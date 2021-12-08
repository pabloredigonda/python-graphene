import os


class GrapheneConfiguration:
    def __init__(self):
        pass

    @staticmethod
    def graphene_debug() -> bool:
        return os.getenv('GRAPHENE_DEBUG') == 'True'

    @staticmethod
    def graphene_host() -> bool:
        return os.getenv('GRAPHENE_HOST')

    @staticmethod
    def graphene_graphiql() -> bool:
        return os.getenv('GRAPHENE_GRAPHIQL') == 'True'
