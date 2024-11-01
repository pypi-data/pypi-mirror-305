import requests


class HttpClient:

    def __init__(self, api_key: str):

        self.api = "http://127.0.0.1:5000"

        self.headers = {
            "X-Session-Token": api_key,
            "Content-Type": "application/json"
        }


    def __parse_response(self, payload: bytes):
        try:
            data = payload.decode("utf-8")
            return data
        except Exception as e:
            print("__parse_response", e)
            return None


    def get(self, url):
        try:
            response = requests.get(f"{self.api}/{url}", headers=self.headers)
            print(response.connection)
            print(response.headers)
            print(response.status_code)
            print(response.content)
            return self.__parse_response(response.content)
        except Exception as e:
            print("Exception", e)
            return {}


    def post(self, url, data):
        try:
            response = requests.post(f"{self.api}/{url}", data, headers=self.headers)
            print(response)
            return self.__parse_response(response.content)
        except Exception as e:
            print("Exception", e)
            return {}


    def put(self, url, data):
        try:
            response = requests.put(f"{self.api}/{url}", data, headers=self.headers)
            print(response)
            return self.__parse_response(response.content)
        except Exception as e:
            print("Exception", e)
            return {}


    def delete(self, url):
        try:
            response = requests.delete(f"{self.api}/{url}", headers=self.headers)
            print(response)
            return self.__parse_response(response.content)
        except Exception as e:
            print("Exception", e)
            return {}
