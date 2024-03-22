#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   send_api.py
@Time    :   2024/03/21 20:49:59
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
import requests
import sys
# sys.path.append("/Users/xiaofengzai/Desktop/industry_llm")
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from config.loggers import logger

# 测试api的效果
def get_post(message: str):
    try:
        # embedding url
        url = "http://localhost:8080/get_recenty/"
        body = {
            "text": message
        }
        # 请求失败时，可重试3次
        s = requests.Session()
        s.mount("https://", HTTPAdapter(max_retries=Retry(total=3, allowed_methods=frozenset(['POST']))))
        # 获取embedding响应
        response = s.post(url, json=body)
        data = response.json()
        return data
    except Exception as e:
        logger.error(f"请求向量数据失败，错误原因：{e}")
        print(f"请求向量数据失败，错误原因：{e}")


if __name__ == '__main__':
    message= "给我2023年8月9日的数据"
    # message= "给我2023年8月的数据"
    print(get_post(message))
