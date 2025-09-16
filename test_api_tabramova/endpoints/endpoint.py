import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    object_id = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name: str):
        assert self.json['name'] == name

    @allure.step('Check that update data is correct')
    def check_response_name_is_updated(self, name: str):
        assert self.response.json()['name'] == name

    @allure.step('Get object data output')
    def print_result_objects(self, object_id):
        print(object_id)

    @allure.step('Check that color is the same as sent')
    def check_response_color_is_correct(self, color: str):
        assert self.json['data']['color'] == color

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200
