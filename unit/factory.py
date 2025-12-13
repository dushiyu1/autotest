#装饰器
import json
from functools import wraps

import allure


def login(func):
    @wraps(func)
    def warpper(*args,**kwargs):
        print("登录开始=======")
        return func(*args,**kwargs)
    return warpper


import logging
from functools import wraps

# 配置日志（一次即可）
logging.basicConfig(level=logging.INFO)

def log_calls(logger=None):
    """通用日志装饰器"""
    def decorator(func):
        log = logger or logging.getLogger(func.__module__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.info(f"→ 调用 {func.__name__}({args}, {kwargs})")
            try:
                result = func(*args, **kwargs)
                log.info(f"← {func.__name__} 返回: {result}")
                return result
            except Exception as e:
                log.error(f"✗ {func.__name__} 抛出异常: {e}")
                raise
        return wrapper
    return decorator

@log_calls()
def tet(a,b):
    return a/b

# print(tet(1,0))

#
# def allure_attach(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         all = allure.attach(
#                 json.dumps(f"url:{url},body:{body}", indent=2, ensure_ascii=False),  # 格式化 JSON 字符串
#                 name="请求参数",
#                 attachment_type=allure.attachment_type.JSON
#             )
#         return func(*args,**kwargs)
#     return wrapper