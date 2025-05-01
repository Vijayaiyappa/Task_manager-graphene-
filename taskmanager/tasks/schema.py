import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from .models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class TaskQuery(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)

    @login_required
    def resolve_all_tasks(self, info):
        return Task.objects.filter(assigned_to=info.context.user)
