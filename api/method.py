import requests


class Methods:

    @staticmethod
    def get_current_weather(api_key, base_url, city_id):
        response = requests.get(f'{base_url}current?city_id={city_id}&key={api_key}&include=minutely')
        return response

    @staticmethod
    def get_alert(api_key, base_url, city_id):
        response = requests.get(f'{base_url}alerts?city_id={city_id}&key={api_key}')
        return response

    @staticmethod
    def get_future_weather(api_key, base_url, city_name):
        response = requests.get(f'{base_url}forecast/daily=16?city={city_name}key={api_key}')
        # response = requests.get(f'https://api.weatherbit.io/v2.0/history/agweather?lat=34.035&lon=-117.846191&start_date=2023-08-23&end_date=2023-08-24&key={api_key}')
        return response

    @staticmethod
    def get_air_quality(api_key, base_url, city_name):
        response = requests.get(f'{base_url}forecast/airquality?city={city_name}&key={api_key}')
        return response

    @staticmethod
    def get_historical(api_key, base_url):
        response = requests.get(f'{base_url}history/agweather?lat=34.035&lon=-117.846191&start_date=2023-08-23&end_date=2048-08-24&key={api_key}')
        return response