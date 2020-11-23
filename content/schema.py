from graphene_django import DjangoObjectType
from content.models import CharacterModel, AscendancyModel


class CharacterType(DjangoObjectType):
    class Meta:
        model = CharacterModel


class AscendancyType(DjangoObjectType):
    class Meta:
        model = AscendancyModel
