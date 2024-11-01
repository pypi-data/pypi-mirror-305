import graphene
from graphene_django import DjangoObjectType

from core import ExtendedConnection
from .models import Control


class ControlGQLType(DjangoObjectType):
    class Meta:
        model = Control
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'adjustability': ['exact', 'icontains', 'istartswith'],
            'usage': ['exact', 'icontains', 'istartswith'],
        }
        connection_class = ExtendedConnection
