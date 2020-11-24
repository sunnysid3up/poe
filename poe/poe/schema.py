import content.schema
import graphene


class Query(content.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
