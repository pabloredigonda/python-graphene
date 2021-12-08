# Python Graphene API

This is a GraphQl API written in Python(Flask/ Graphene).

## Usage

A Make File is provided for convenience:

 - **make compose** - creates and set up the containers
 - **make down** - stop containers
 - **make test** - run tests
 - **make drop** - drop the docker images
 - **make python** - go inside the python container
 - **make mongo** - go inside the mongo container

Or you can run the docker commands:

 - **docker-compose up -d** - creates and set up the containers
 - **docker exec python-graphene pytest -s** - run tests
 