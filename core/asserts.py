import json
from requests import Response


class Asserts:
    @staticmethod
    def assert_equals(val1, val2, error_massage: str = ""):
        assert val1 == val2, f"Failed assertion that {val1} is equals {val2}. {error_massage}"

    @staticmethod
    def assert_code_status(response: Response, expected_code: int, message: str = ""):
        assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {response.text}'

    @staticmethod
    def assert_json_value_by_key(response: Response, key: str, val: str):
        try:
            response_as_dict = response.json()['data'][0]
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does\'n have key "{key}"'

        assert response_as_dict[key] == val, \
            f'Response key "{key}" has value {response_as_dict[key]} but expected is {val}'

    @staticmethod
    def assert_temperature_is_normal(response: Response):
        try:
            response_as_dict = response.json()['data'][0]
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert (-93 < response_as_dict['temp'] < 57), \
        f'{response_as_dict["temp"]} is non-valid temperature' #Максимум и минимум на нашей планете

    @staticmethod
    def assert_json_has_key(response: Response, key: str):
        try:
            response_as_dict = response.json()['data'][0]
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does not have a key "{key}" which is expected. JSON text: "{response.text}"'

    @staticmethod
    def assert_text_fail(response: Response, text: str):
        assert response.json()["error"] == text, \
            f'Expected text: {text}, actual text: {response.json()["error"]}'

    @staticmethod
    def assert_correct_type(response: Response, key: str, type_answer: type):
        assert isinstance(response.json()['data'][0][f"{key}"], type_answer), \
            f'Expected type: {type_answer}, actual type: {type(response.json()["data"][0][f"{key}"])}'
