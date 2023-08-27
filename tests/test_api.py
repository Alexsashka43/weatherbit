import allure
import pytest

from api.method import Methods
from core.asserts import Asserts


@allure.title("Air quality")
def test_air_quality(api_key, base_url):
    response = Methods.get_air_quality(api_key, base_url, city_name='Almaty')
    Asserts.assert_code_status(response, 200)
    Asserts.assert_json_has_key(response, 'aqi') #Air Quality Index


@pytest.mark.smoke
@pytest.mark.regress
@allure.step
@allure.title("Сurrent weather")
@pytest.mark.parametrize("city_id,city", [('8953651', 'Martini'),
                                          ('8953662', 'Aiola'),
                                          ('8953706', 'Boscazzo'),
                                          pytest.param('0', 'Null', marks=pytest.mark.xfail)])
def test_get_current_weather(api_key, base_url, city_id, city):
    response = Methods.get_current_weather(api_key, base_url, city_id)
    Asserts.assert_code_status(response, 200)
    Asserts.assert_json_value_by_key(response, 'city_name', city)
    Asserts.assert_temperature_is_normal(response)


@pytest.mark.smoke
@pytest.mark.regress
@allure.step
@allure.title("Alert")
@pytest.mark.parametrize("city_id", ['1526384', '1526273', '1526274', '1526443', '1526522', '1526573', '1526601',
                                     '1526619'])
def test_get_alert(api_key, base_url, city_id):
    response = Methods.get_alert(api_key, base_url, city_id)
    Asserts.assert_code_status(response, 200)


@allure.title("Historical Ag-Weather")
def test_negative_historical(api_key, base_url):
    response = Methods.get_historical(api_key, base_url)
    Asserts.assert_code_status(response, 400)
    Asserts.assert_text_fail(response, 'Requested date range too large.')


@pytest.mark.regress
@allure.step
@allure.title("Future weather")
def test_negative_get_future_weather(api_key, base_url, city_name='Astana'):
    response = Methods.get_future_weather(api_key, base_url, city_name)
    Asserts.assert_code_status(response, 403) #the requested resource is forbidden



