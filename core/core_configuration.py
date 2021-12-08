import os
import string


class CoreConfiguration:
    def __init__(self):
        pass

    @staticmethod
    def mariadb_host() -> string:
        return str(os.getenv('MARIADB_HOST'))

    @staticmethod
    def mariadb_user() -> string:
        return str(os.getenv('MARIADB_USER'))

    @staticmethod
    def mariadb_password() -> string:
        return str(os.getenv('MARIADB_PASSWORD'))

    @staticmethod
    def mariadb_database() -> string:
        return str(os.getenv('MARIADB_DATABASE'))
