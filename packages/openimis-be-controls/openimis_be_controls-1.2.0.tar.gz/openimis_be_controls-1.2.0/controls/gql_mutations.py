import logging

import graphene
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError, PermissionDenied
from django.db import transaction
from graphene import InputObjectType

from contribution.apps import ContributionConfig
from contribution.gql_mutations import PremiumBase, update_or_create_premium
from contribution.models import Premium
from controls.models import MobileEnrollmentMutation as MobileMutationLog
from core.schema import OpenIMISMutation
from insuree.apps import InsureeConfig
from insuree.gql_mutations import FamilyBase, InsureeBase
from insuree.services import FamilyService, InsureeService
from policy.apps import PolicyConfig
from policy.gql_mutations import PolicyInputType
from policy.models import Policy
from policy.services import PolicyService

logger = logging.getLogger(__name__)


class PremiumEnrollmentGQLType(PremiumBase, InputObjectType):
    policy_id = graphene.Int(required=True)


class PolicyEnrollmentGQLType(PolicyInputType, InputObjectType):
    mobile_id = graphene.Int(required=True)


class InsureeEnrollmentGQLType(InsureeBase, InputObjectType):
    pass


class FamilyEnrollmentGQLType(FamilyBase, InputObjectType):
    pass


class MobileEnrollmentGQLType:
    family = graphene.Field(FamilyEnrollmentGQLType, required=True)
    insurees = graphene.List(InsureeEnrollmentGQLType)  # for families with more than the head insuree
    policies = graphene.List(PolicyEnrollmentGQLType, required=True)
    premiums = graphene.List(PremiumEnrollmentGQLType, required=True)


MOBILE_ENROLLMENT_RIGHTS = sum([
    InsureeConfig.gql_mutation_create_families_perms,
    InsureeConfig.gql_mutation_update_families_perms,
    InsureeConfig.gql_mutation_create_insurees_perms,
    InsureeConfig.gql_mutation_update_insurees_perms,
    PolicyConfig.gql_mutation_create_policies_perms,
    PolicyConfig.gql_mutation_edit_policies_perms,
    ContributionConfig.gql_mutation_create_premiums_perms,
    ContributionConfig.gql_mutation_update_premiums_perms
], [])


class MobileEnrollmentMutation(OpenIMISMutation):
    _mutation_module = "controls"
    _mutation_class = "MobileEnrollmentMutation"

    class Input(MobileEnrollmentGQLType, OpenIMISMutation.Input):
        pass

    @classmethod
    def async_mutate(cls, user, **data):
        logger.info("Receiving new mobile enrollment request")
        logger.info(data)
        try:
            if type(user) is AnonymousUser or not user.id:
                raise ValidationError("mutation.authentication_required")
            if not user.has_perms(MOBILE_ENROLLMENT_RIGHTS, list_evaluation_or=True):
                raise PermissionDenied("unauthorized")

            with transaction.atomic():  # either everything succeeds, or everything fails
                from core.utils import TimeUtils
                now = TimeUtils.now()
                # Cleaning up None values received from the mobile app
                cleaned_data = delete_none(data)
                family_data = cleaned_data["family"]
                insuree_data = cleaned_data["insurees"]
                policy_data = cleaned_data["policies"]
                premium_data = cleaned_data["premiums"]
                client_mutation_id = cleaned_data["client_mutation_id"]

                # 1 - Creating/Updating the family with the head insuree
                logger.info(f"Creating/Updating the family with head insuree {family_data['head_insuree']['chf_id']}")
                family_data.pop("id")
                add_audit_values(family_data, user.id_for_audit, now)
                family = FamilyService(user).create_or_update(family_data)

                # 2 - Creating/Updating the remaining insurees
                for insuree in insuree_data:
                    logger.info(f"Creating/Updating insuree {insuree['chf_id']}")
                    add_audit_values(insuree, user.id_for_audit, now)
                    insuree["family_id"] = family.id
                    InsureeService(user).create_or_update(insuree)

                # 3 - Creating/Updating policies
                policy_ids_mapping = {}  # storing the mobile internal IDs and their related backend UUIDs b/c premiums need UUIDs
                for current_policy_data in policy_data:
                    logger.info(f"Creating/Updating a policy for family {family.id}")
                    mobile_id = current_policy_data.pop("mobile_id")  # Removing the mobile internal ID
                    add_audit_values(current_policy_data, user.id_for_audit, now)
                    current_policy_data["family_id"] = family.id

                    if "uuid" not in current_policy_data:
                        # It means it's a creation. These fields are added by the CreatePolicyMutation before calling the service
                        current_policy_data["status"] = Policy.STATUS_IDLE
                        current_policy_data["stage"] = Policy.STAGE_NEW

                    policy = PolicyService(user).update_or_create(current_policy_data, user)
                    policy_ids_mapping[mobile_id] = policy.id  # Storing the backend UUID

                # 4 - Creating/Updating premiums
                for current_premium_data in premium_data:
                    logger.info(f"Creating/Updating a premium for family {family.id} and policy {policy.id}")
                    add_audit_values(current_premium_data, user.id_for_audit, now)
                    mobile_policy_id = current_premium_data.pop("policy_id")
                    current_premium_data.pop("policy_uuid", None)
                    current_premium_data["policy_id"] = policy_ids_mapping[mobile_policy_id]
                    current_premium_data["is_offline"] = False
                    # There is no PremiumService, so we're using directly the function in the gql_mutations file
                    update_or_create_premium(Premium(**current_premium_data), user)

                MobileMutationLog.object_mutated(user, client_mutation_id=client_mutation_id, policy=policy)
                logger.info(f"Mobile enrollment processed successfully!")
                return None
        except Exception as exc:
            return [
                {
                    'message': "core.mutation.failed_to_enroll",
                    'detail': str(exc)
                }]


def add_audit_values(data: dict, user_id: int, now):
    data["validity_from"] = now
    data["audit_user_id"] = user_id


# Somehow, the library used for preparing GQL queries and sending data is not able to remove fields that have a null value
# Since the current GQL/Graphene/... version does not support null values, everything is built thinking we won't have null values, and here, we do
# It breaks things (imagine having a UUID=None) so we need to clean data before sending it to the various services
# Function taken from https://stackoverflow.com/a/66127889
def delete_none(_dict):
    for key, value in list(_dict.items()):
        if isinstance(value, dict):
            delete_none(value)
        elif value is None:
            del _dict[key]
        elif isinstance(value, list):
            for v_i in value:
                if isinstance(v_i, dict):
                    delete_none(v_i)
    return _dict
