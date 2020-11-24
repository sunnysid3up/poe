import graphene
import content.schema


class Query(content.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
