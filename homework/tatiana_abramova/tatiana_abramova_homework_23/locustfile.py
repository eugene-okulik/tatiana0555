from locust import task, HttpUser
import random


class ObjectUser(HttpUser):

    def on_start(self):
        self.object_id = None

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object',
            headers={'Content-Type': 'application/json'}
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice([1, 513, 514, 516, 520])}',
            headers={'Content-Type': 'application/json'}
        )

    @task(2)
    def post_one_object(self):
        response = self.client.post(
            '/object',
            json={"name": "test_object", "data": {"color": "green", "size": "medium"}},
            headers={'Content-Type': 'application/json'}
        )
        self.object_id = response.json()['id']
        self.client.delete(
            f'/object/{self.object_id}'
        )

    @task(1)
    def put_object(self):
        create_test_object = self.client.post(
            '/object',
            json={"name": "test object2", "data": {"color": "yellow", "size": "big"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = create_test_object.json()['id']
        self.client.put(
            f'/object/{self.object_id}',
            json={"name": "Updated object", "data": {"color": "black", "size": "small"}},
            headers={"Content-Type": "application/json"}
        )
        self.client.delete(
            f'/object/{self.object_id}'
        )

    @task(1)
    def patch_object(self):
        create_test_object = self.client.post(
            '/object',
            json={"name": "test object3", "data": {"color": "white", "size": "small"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = create_test_object.json()['id']
        self.client.patch(
            f'/object/{self.object_id}',
            json={"name": "Patched name"},
            headers={"Content-Type": "application/json"}
        )
        self.client.delete(
            f'/object/{self.object_id}'
        )

    @task(1)
    def delete_object(self):
        create_test_object = self.client.post(
            '/object',
            json={"name": "Deleted object", "data": {"color": "black", "size": "big"}},
            headers={"Content-Type": "application/json"}
        )
        self.object_id = create_test_object.json()['id']
        self.client.delete(
            f'/object/{self.object_id}'
        )
