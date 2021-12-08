import logging
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    event,
)
from sqlalchemy.orm import mapper, relationship

from core.department.domain.Department import Department

logger = logging.getLogger(__name__)

metadata = MetaData()

departmentsTable = Table(
    "departments",
    metadata,
    Column("department_id", Integer, primary_key=True, nullable=False),
    Column("name", String(255)),
    mariadb_engine="InnoDB",
    mysql_engine="InnoDB",
)


def start_mappers():
    mapper(
        Department,
        departmentsTable,
    )
