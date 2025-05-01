import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
import graphql_jwt
from tasks.schema import TaskQuery

class Query(UserQuery, MeQuery, TaskQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
