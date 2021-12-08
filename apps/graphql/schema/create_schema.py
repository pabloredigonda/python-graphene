from graphene import Schema
import graphene

from core.core_app import CoreApp
from .department import create_department_mutation_builder, DepartmentType
from apps.graphql.department.list.list_departments_query import ListDepartmentsQuery


def create_schema(core: CoreApp):
    class Mutations(graphene.ObjectType):
        create_department = create_department_mutation_builder(core.createDepartmentService())

    class Queries(graphene.ObjectType):
        node = graphene.relay.Node.Field()
        list_departments = graphene.List(DepartmentType)

        @staticmethod
        def resolve_list_departments(root, info):
            query = ListDepartmentsQuery(core.listDepartmentsService())
            return query()

    return Schema(query=Queries, mutation=Mutations)
