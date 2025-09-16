import pytest

TEST_DATA = [
    {"name": "Third object", "data": {"color": "yellow", "size": "big"}},
    {"name": "Fourth object", "data": {"color": "green", "size": "medium"}},
    {"name": "Fifth object", "data": {"color": "white", "size": "small"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_an_object(create_object_endpoint, data, delete_object_endpoint):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_that_status_is_200()
    object_id = create_object_endpoint.object_id

    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()


def test_update_object_put(update_object_endpoint, new_object_id):
    updated_data = {'name': 'Updated Object', "data": {"color": "black", "size": "small"}}
    update_object_endpoint.make_changes_in_object(new_object_id, updated_data)
    update_object_endpoint.check_response_name_is_updated(updated_data['name'])
    update_object_endpoint.check_that_status_is_200()


def test_update_object_patch(update_object_endpoint, new_object_id):
    updated_data = {'name': 'Patched Name'}
    update_object_endpoint.patch_object(new_object_id, updated_data)
    update_object_endpoint.check_response_name_is_updated(updated_data['name'])
    update_object_endpoint.check_that_status_is_200()


def test_delete_object(create_object_endpoint, delete_object_endpoint):
    body = {
        "name": "Temp object",
        "data": {"color": "blue", "size": "tiny"}
    }
    create_object_endpoint.create_new_object(body)
    object_id = create_object_endpoint.object_id
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()
