import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture(autouse=True, scope='session')
def start_end_text():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True, scope='function')
def each_test_text():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def new_object_id(create_object_endpoint, delete_object_endpoint):
    body = {
        "name": "First object",
        "data": {"color": "white", "size": "big"}
    }
    create_object_endpoint.create_new_object(body)
    object_id = create_object_endpoint.object_id
    yield object_id
    delete_object_endpoint.delete_object(object_id)
