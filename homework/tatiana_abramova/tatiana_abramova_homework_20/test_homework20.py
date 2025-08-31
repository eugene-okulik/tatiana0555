import requests
import pytest


@pytest.fixture(scope='session')
def start_end_text():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def each_test_text():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def create_delete_test_object():
    body = {
        "name": "First object",
        "data": {"color": "white", "size": "big"}
        }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    obj_id = request.json()['id']
    yield obj_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')


@pytest.fixture()
def create_test_object():
    body = {
        "name": "test_name",
        "data": {"color": "blue", "size": "medium"}
    }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    obj_id = request.json()['id']
    return obj_id


@pytest.mark.critical
@pytest.mark.parametrize('color, size, name',
                         [
                             ("yellow", "big", "Third object"),
                             ("green", "medium", "Fourth object"),
                             ("white", "small", "Fifth object"),
                         ])
def test_create_object(color, size, name, start_end_text, each_test_text):
    body = {
        "data": {
            "color": color,
            "size": size
        },
        "name": name,
    }
    request = requests.post('http://objapi.course.qa-practice.com/object', json=body)
    assert request.status_code == 200, "Wrong status code"


@pytest.mark.medium
def test_put_a_object(create_delete_test_object, each_test_text):
    body = {
        "name": "Updated Object",
        "data": {"color": "black", "size": "small"}
    }
    request = requests.put(f'http://objapi.course.qa-practice.com/object/{create_delete_test_object}', json=body)
    assert request.status_code == 200


def test_patch_object(create_delete_test_object, each_test_text):
    body = {"name": "Patched Name"}
    request = requests.patch(f'http://objapi.course.qa-practice.com/object/{create_delete_test_object}', json=body)
    assert request.status_code == 200


def test_delete_object(create_test_object, each_test_text):
    request = requests.delete(f'http://objapi.course.qa-practice.com/object/{create_test_object}')
    assert request.status_code == 200
