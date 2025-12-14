import allure
import requests
from requests import request


class Test_01():

    with allure.step("请求"):
        def test_001(self):
            response = requests.get('http://localhost:8080/api/red-list')
            print(response.text)
            assert response




