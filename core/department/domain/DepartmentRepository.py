from core.department.domain.Department import Department


class DepartmentRepository:
    def list(self) -> []:
        raise NotImplementedError()

    def save(self, department: Department):
        raise NotImplementedError()
