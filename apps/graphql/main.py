import sys

sys.path.append("/app")

from graphene_app import GrapheneApp
from dotenv import load_dotenv


def run():
    load_dotenv()
    GrapheneApp()


if __name__ == '__main__':
    run()
