from graphene_django import DjangoObjectType
from content.models import AscendancyModel, CharacterModel, PassiveSkillModel


class CharacterType(DjangoObjectType):
    class Meta:
        model = CharacterModel


class AscendancyType(DjangoObjectType):
    class Meta:
        model = AscendancyModel


class PassiveSkillType(DjangoObjectType):
    class Meta:
        model = PassiveSkillModel
