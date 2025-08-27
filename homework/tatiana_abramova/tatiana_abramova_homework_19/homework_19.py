import requests

BASE_URL = "http://objapi.course.qa-practice.com"


def create_object():
    body = {
        "name": "First object",
        "data": {"color": "white", "size": "big"}
    }
    response = requests.post(f"{BASE_URL}/object", json=body)
    print("CREATE:", response.status_code, response.json())
    return response.json().get("id")


def update_object_put(obj_id):
    body = {
        "name": "Updated Object",
        "data": {"color": "black", "size": "small"}
    }
    response = requests.put(f"{BASE_URL}/object/{obj_id}", json=body)
    print("PUT:", response.status_code, response.json())


def update_object_patch(obj_id):
    body = {
        "name": "Patched Name"
    }
    response = requests.patch(f"{BASE_URL}/object/{obj_id}", json=body)
    print("PATCH:", response.status_code, response.json())


def delete_object(obj_id):
    response = requests.delete(f"{BASE_URL}/object/{obj_id}")
    print("DELETE:", response.status_code)


obj_id = create_object()
update_object_put(obj_id)
update_object_patch(obj_id)
delete_object(obj_id)
