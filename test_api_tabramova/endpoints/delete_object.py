import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete the object')
    def delete_object(self, object_id, body=None, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        return self.response
