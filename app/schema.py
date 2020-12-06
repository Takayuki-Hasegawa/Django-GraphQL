import graphene
from graphene_django import DjangoObjectType
from .models import UserTable


class UserTableType(DjangoObjectType):
    class Meta:
        model = UserTable


class Query (graphene.ObjectType):
    userTables = graphene.List(MemberType)
    userTable = (MemberType, id=graphene.Int())

    def resolve_userTables(self, info, **kwargs):
        return UserTable.objects.all()

    def resolve_userTable(self, info, **kwargs):
        id = kwargs.get('id')
        return UserTable.objects.get(pk=id)
