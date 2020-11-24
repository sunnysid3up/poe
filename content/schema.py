from django.db.models import Q
import graphene
from content.models import AscendancyModel, CharacterModel, PassiveSkillModel
from content.types import AscendancyType, CharacterType, PassiveSkillType


class Query(graphene.ObjectType):
    characters = graphene.List(CharacterType)
    ascendants = graphene.List(AscendancyType, character=graphene.String())
    passive_skills = graphene.List(PassiveSkillType, search=graphene.String())

    def resolve_characters(self, info, **kwargs):
        return CharacterModel.objects.all()

    def resolve_ascendants(self, info, character=None):
        if character:
            return AscendancyModel.objects.filter(character__name__exact=character)
        return AscendancyModel.objects.all()

    def resolve_passive_skills(self, info, search=None):
        if search:
            custom_filter = (
                Q(name__icontains=search)
                | Q(ascendancy__name__exact=search)
                | Q(skill_type__exact=search)
                | Q(stats__icontains=search)
            )
            return PassiveSkillModel.objects.filter(custom_filter)

        return PassiveSkillModel.objects.all()


schema = graphene.Schema(query=Query)
