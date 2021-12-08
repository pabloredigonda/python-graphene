from abc import ABC

from core.department.domain.DepartmentRepository import DepartmentRepository
from ..domain.Department import Department


class SqlAlchemyDepartmentRepository(DepartmentRepository, ABC):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def list(self) -> []:
        return self.session.query(Department).all()

    def save(self, department: Department):
        self.session.add(department)
        self.session.commit()
