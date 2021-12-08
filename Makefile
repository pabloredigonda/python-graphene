.PHONY: start up install down test python mongo drop

MAKEPATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PWD := $(dir $(MAKEPATH))

start:
	docker exec -it python-graphene python3 apps/graphql/main.py
up:
	docker-compose up -d

install :
	docker exec -it python-graphene pip3 install -r /app/requirements.txt

down :
	docker stop python-graphene && docker rm python-graphene

test:
	docker exec -it python-graphene pytest -s

python:
	docker exec -it python-graphene bash

mongo:
	docker exec -it python-graphene-mongodb mongo

drop :
	docker rmi python_python-api