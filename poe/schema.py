from django.db.models import Q
import graphene
from content.models import AscendancyModel, CharacterModel, PassiveSkillModel
from content.schema import AscendancyType, CharacterType, PassiveSkillType


class Query(graphene.ObjectType):
    all_characters = graphene.List(CharacterType)
    all_ascendancies = graphene.List(AscendancyType)
    all_passive_skills = graphene.List(PassiveSkillType, search=graphene.String())

    def resolve_all_characters(self):
        return CharacterModel.objects.all()

    def resolve_all_ascendancies(self):
        return AscendancyModel.objects.all()

    def resolve_all_passive_skills(self, info, search=None):
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
