import sys

sys.path.append("/app")

from test.apps.graphql.bootstrap import execute_query, insert_department, clear_db, end


def test_list_departments():
    pass
    # give_i_have_some_departments()
    # response = when_i_query_list_departments()
    # i_spect_a_list_of_departments(response)


def give_i_have_some_departments():
    clear_db()
    insert_department(1, "Department 1")
    insert_department(2, "Department 2")
    insert_department(3, "Department 3")
    clear_db()
    end()


def when_i_query_list_departments():
    return execute_query('''
            query{
                listDepartments{
                    departmentId
                    name
                }
            }
            ''')


def i_spect_a_list_of_departments(executed):
    assert executed == {
        "data": {
            "listDepartments": [
                {
                    "departmentId": 1,
                    "name": "Department 1"
                },
                {
                    "departmentId": 2,
                    "name": "Department 2"
                },
                {
                    "departmentId": 3,
                    "name": "Department 3"
                }
            ]
        }
    }