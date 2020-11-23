from graphene_django import DjangoObjectType
from lore.models import CharacterModel


class CharacterType(DjangoObjectType):
    class Meta:
        model = CharacterModel

