from apps.graphql.schema.department import CreateDepartmentInput
from core.department.action.create.CreateDepartmentService import CreateDepartmentService
from core.shared.infrastructure.unit_of_work import SqlAlchemyUnitOfWork


class CreateDepartmentMutation:
    def __init__(self):
        uow = SqlAlchemyUnitOfWork()
        with uow:
            self.__service = CreateDepartmentService(uow.departmentRepository)

    def __call__(self, input: CreateDepartmentInput):
        department = self.__service(input.name)
        return department
