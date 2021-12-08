from core.department.domain import DepartmentRepository


class ListDepartmentsService:
    def __init__(self, repository: DepartmentRepository):
        self.__repository = repository

    def __call__(self):
        return self.__repository.list()
