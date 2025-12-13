#放测试夹具,pytest从这里加载夹具
import json

import allure
import pytest
import requests
from requests import request


# @pytest.fixture(scope="function")
# def login():
#     all = allure.attach(
#         json.dumps(f"url:{url},body:{body}", indent=2, ensure_ascii=False),  # 格式化 JSON 字符串
#         name="请求参数",
#         attachment_type=allure.attachment_type.JSON
#     )
#     return all

