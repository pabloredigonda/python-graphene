# Python Graphene API

## Create Department Mutation
Mutation
```
mutation{
  createDepartment(input: {
    name: "Department 3"
  }){
    department{
      departmentId
      name
    }
    result{
      success
      errorCode
      errorMessage
    }
  }
}
```

Response
```
{
  "data": {
    "createDepartment": {
      "department": {
        "departmentId": 1,
        "name": "Department 3"
      },
      "result": {
        "success": true,
        "errorCode": null,
        "errorMessage": null
      }
    }
  }
}
```

## Create Department Mutation
Query
```
query{
  listDepartments{
    departmentId
    name
  }
}
```
Response
```
{
  "data": {
    "listDepartments": [
      {
        "departmentId": 1,
        "name": "Department 1"
      }
    ]
  }
}
```

## Install dependencies
```
make install
```

## Start Docker containers
```
make up
```

## Start GraphQL Server
```make
make start
```

## Run Tests
```make
make test
```



## Stack
- [Python](https://www.python.org/)
- [Graphene](https://graphene-python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [MariaDB](https://mariadb.org/)
- [GraphQL](https://graphql.org/)
- [Docker](https://www.docker.com/)
- [PyTest](https://docs.pytest.org/en/6.2.x/)
- [SQL Alchemy](https://www.sqlalchemy.org/)


