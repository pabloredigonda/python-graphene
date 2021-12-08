# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.session import Session

from core.core_configuration import CoreConfiguration
from core.department.domain.DepartmentRepository import DepartmentRepository
from core.department.infrastructure.SqlAlchemyDepartmentRepository import SqlAlchemyDepartmentRepository


class AbstractUnitOfWork(abc.ABC):
    departmentRepository: DepartmentRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for product in self.products.seen:
            while product.events:
                yield product.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


host = CoreConfiguration.mariadb_host()
user = CoreConfiguration.mariadb_user()
password = CoreConfiguration.mariadb_password()
database = CoreConfiguration.mariadb_database()
engine = create_engine(f"mariadb+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4")
DEFAULT_SESSION_FACTORY = scoped_session(sessionmaker(autocommit=False,
                                                      autoflush=False,
                                                      bind=engine))


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.departmentRepository = SqlAlchemyDepartmentRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
