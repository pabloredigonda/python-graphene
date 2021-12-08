from core.department.action.create.CreateDepartmentService import CreateDepartmentService
from core.department.action.list.ListDepartmentsService import ListDepartmentsService
from core.shared.infrastructure.orm import start_mappers
from core.shared.infrastructure.unit_of_work import SqlAlchemyUnitOfWork


class CoreApp:
    def __init__(self):
        start_mappers()
        self.__uow = SqlAlchemyUnitOfWork()
        with self.__uow:
            self.__createDepartmentService = CreateDepartmentService(self.__uow.departmentRepository)
            self.__listDepartmentsService = ListDepartmentsService(self.__uow.departmentRepository)

    def createDepartmentService(self) -> CreateDepartmentService:
        return self.__createDepartmentService

    def listDepartmentsService(self) -> ListDepartmentsService:
        return self.__listDepartmentsService
