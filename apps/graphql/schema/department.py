import graphene

from apps.graphql.shared.mutation_result_type import MutationResultType, SuccessMutationResultType
from core.department.action.create.CreateDepartmentService import CreateDepartmentService


class CreateDepartmentInput(graphene.InputObjectType):
    name = graphene.String(required=True)


class DepartmentType(graphene.ObjectType):
    departmentId = graphene.Int(required=True)
    name = graphene.String(required=True)


def create_department_mutation_builder(service: CreateDepartmentService):
    class CreateDepartmentMutation(graphene.Mutation):
        class Arguments:
            input = CreateDepartmentInput(required=True)

        department = graphene.Field(DepartmentType)
        result = graphene.Field(MutationResultType)

        @staticmethod
        def mutate(root, info, input=CreateDepartmentInput):
            departmentModel = service(input.name)
            department = DepartmentType(departmentModel.getId(), departmentModel.getName())

            result = SuccessMutationResultType()

            return CreateDepartmentMutation(department=department, result=result)

    return CreateDepartmentMutation.Field()
