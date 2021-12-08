import sys

sys.path.append("/app")

import string
from test.apps.graphql.bootstrap import execute_query, clear_db, end


def create_department_mutation(name: string):
    return '''
        mutation {
            createDepartment(input: { name: "''' + name + '''" }) {
                department {
                    departmentId
                    name
                }
                result {
                    success
                    errorCode
                    errorMessage
                }
            }
        }
    '''


def test_create_department():
    clear_db()
    response = when_i_mutate_create_department()
    i_spect_a_success_response(response)
    clear_db()
    end()


def when_i_mutate_create_department():
    return execute_query(create_department_mutation('Department 1'))


def i_spect_a_success_response(executed):
    assert_success_result(executed)

    assert type(executed["data"]["createDepartment"]["department"]["departmentId"]) is int
    assert executed["data"]["createDepartment"]["department"]["name"] == "Department 1"


def assert_success_result(executed):
    assert executed["data"]["createDepartment"]["result"] == {
        "success": True,
        "errorCode": None,
        "errorMessage": None
    }