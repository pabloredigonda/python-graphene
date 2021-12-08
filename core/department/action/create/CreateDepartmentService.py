import string

from core.department.domain.Department import Department
from core.department.domain.DepartmentRepository import DepartmentRepository


class CreateDepartmentService:
    def __init__(self, repository: DepartmentRepository):
        self.__repository = repository

    def __call__(self, name: string) -> Department:
        department = Department(None, name)
        self.__repository.save(department)
        return department
