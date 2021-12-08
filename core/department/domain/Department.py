import string
from core.shared.domain.AggregateRoot import AggregateRoot


class Department(AggregateRoot):
    def __init__(self, department_id: int, name: string):
        super().__init__()
        self.department_id = department_id
        self.name = name

    def getName(self) -> string:
        return self.name

    def getId(self) -> int:
        return self.department_id
