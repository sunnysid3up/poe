import graphene
from content.models import CharacterModel, AscendancyModel
from content.schema import CharacterType, AscendancyType


class Query(graphene.ObjectType):
    all_characters = graphene.List(CharacterType)
    all_ascendancies = graphene.List(AscendancyType)

    @staticmethod
    def resolve_all_characters(root, info, **kwargs):
        return CharacterModel.objects.all()

    @staticmethod
    def resolve_all_ascendancies(root, info, **kwargs):
        return AscendancyModel.objects.all()


schema = graphene.Schema(query=Query)
