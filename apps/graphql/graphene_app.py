from flask import Flask
from flask_graphql import GraphQLView

from apps.graphql.graphene_configuration import GrapheneConfiguration
from core.core_app import CoreApp
from schema.create_schema import create_schema


class GrapheneApp:
    def __init__(self):
        self.__core = CoreApp()
        self.__app = Flask(__name__)
        self.__app.debug = GrapheneConfiguration.graphene_debug()
        self.__app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view(
                'graphql',
                schema=create_schema(self.__core),
                graphiql=GrapheneConfiguration.graphene_graphiql()
            )
        )

        self.__app.run(debug=GrapheneConfiguration.graphene_debug(), host=GrapheneConfiguration.graphene_host())
