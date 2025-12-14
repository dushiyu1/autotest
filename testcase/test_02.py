import json

import allure
import requests
from requests import request


class Test_02():
    def test_002(self):
        with allure.step("请求"):
            print("aaasdsada")

        with allure.step("新增"):
            url = "http://localhost:8080/api/submit"
            # body = {"gameName":"测试","server":"222","gameId":"测试","userName":"娃哈哈","isRed":True,"description":"这人牛逼啊","screenshotUrl":None}
            response = requests.post(url)
            # allure.attach(
            #     json.dumps(f"url:{url},body:{body}", indent=2,ensure_ascii=False),  # 格式化 JSON 字符串
            #     name="请求参数",
            #     attachment_type=allure.attachment_type.JSON
            # )
            print(response.text)
            assert response




