from apps.graphql.schema.department import DepartmentType
from core.department.action.list.ListDepartmentsService import ListDepartmentsService


class ListDepartmentsQuery:
    def __init__(self, service: ListDepartmentsService):
        self.__service = service

    def __call__(self, *args, **kwargs):
        departmentsList = self.__service()
        return (DepartmentType(department.getId(), department.getName()) for department in departmentsList)
