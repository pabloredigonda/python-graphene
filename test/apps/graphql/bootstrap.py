import os
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('MARIADB_HOST')
user = os.getenv('MARIADB_USER')
password = os.getenv('MARIADB_PASSWORD')
database = os.getenv('MARIADB_DATABASE')
engine = create_engine(f"mariadb+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4")

session_factory = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=engine))

session = session_factory()

GRAPHQL_URL = str(os.getenv('GRAPHQL_URL'))


def clear_db():
    session.execute('DELETE FROM demo.departments')
    session.commit()


def end():
    session.close()


def insert_department(department_id: int, name: string):
    session.execute(f"INSERT INTO departments SET department_id={department_id},name='{name}'")
    session.commit()


def execute_query(query: string):
    response = requests.post(GRAPHQL_URL, json={'query': str(query)})
    return response.json()
