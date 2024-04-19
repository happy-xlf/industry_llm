#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   vanna_test.py
@Time    :   2024/04/19 10:17:09
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

from vanna.remote import VannaDefault
from vanna.openai.openai_chat import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
from vanna.base.base import VannaBase
from vanna.flask import VannaFlaskApp
from openai import OpenAI
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import pymysql
from abc import ABC, abstractmethod
import requests

# client = OpenAI()


# class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
#     def __init__(self, client=None, config=None):
#         ChromaDB_VectorStore.__init__(self, config=config)
#         OpenAI_Chat.__init__(self, client=client, config=config)


# vn = MyVanna(client=client, config={"model": "gpt-3.5-turbo"})

class MyCustomLLM(VannaBase):
    def __init__(self, config=None):
        # Implement here
        self.config = config
        self.run_sql_is_set = False
        self.static_documentation = ""

    @staticmethod
    def system_message(message: str) -> dict:
        return {"role": "system", "content": message}

    @staticmethod
    def user_message(message: str) -> dict:
        return {"role": "user", "content": message}

    @staticmethod
    def assistant_message(message: str) -> dict:
        return {"role": "assistant", "content": message}
    
    def submit_prompt(self, prompt, **kwargs) -> str:
        # Implement here
        # See an example implementation here: https://github.com/vanna-ai/vanna/blob/main/src/vanna/mistral/mistral.py
        url = "http://localhost:9999/multi_chat/"
        body = {
            "text": prompt
        }
        # 请求失败时，可重试3次
        s = requests.Session()
        s.mount("https://", HTTPAdapter(max_retries=Retry(total=3, allowed_methods=frozenset(['POST']))))
        # 获取embedding响应
        response = s.post(url, json=body)
        data = response.json()
        return data

class MyVanna(ChromaDB_VectorStore, MyCustomLLM):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        MyCustomLLM.__init__(self, config=config)

vn = MyVanna()

# vn.max_tokens = 1000
# vn.temperature = 0.1

# MySQL数据库连接参数
conn_details = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "rootroot",
    "database": "industry",
    "charset": "utf8mb4",
}

# 建立MySQL数据库连接
conn = pymysql.connect(**conn_details)


# 定义一个函数,用于执行SQL查询并返回一个Pandas DataFrame
def run_sql(sql: str) -> pd.DataFrame:
    df = pd.read_sql_query(sql, conn)
    return df


# 将函数设置到vn.run_sql中
vn.run_sql = run_sql
vn.run_sql_is_set = True

d1 = """
CREATE TABLE `day_message` (
  `date` varchar(255) NOT NULL COMMENT '日期',
  `opc_raw` float NOT NULL COMMENT 'opc生料日产量',
  `src_raw` float NOT NULL COMMENT 'src生料日产量',
  `mo_day` varchar(255) NOT NULL COMMENT '原料磨日运转率',
  `opc` float NOT NULL COMMENT 'opc熟料日产量',
  `src` float NOT NULL COMMENT 'src熟料日产量',
  `hui_day` varchar(255) NOT NULL COMMENT '回转窑日运转率',
  `zhu` varchar(255) DEFAULT NULL COMMENT '备注信息'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='每日生产信息';

CREATE TABLE `month_message` (
  `date` varchar(255) NOT NULL COMMENT '月份日期',
  `opc_raw` float NOT NULL COMMENT 'OPC生料月产',
  `src_raw` float NOT NULL COMMENT 'SRC生料月产',
  `mo_lv` varchar(255) NOT NULL COMMENT '原料磨月累运转率',
  `opc` float NOT NULL COMMENT 'OPC熟料月产',
  `src` float NOT NULL COMMENT 'SRC熟料月产',
  `hui_lv` varchar(255) NOT NULL COMMENT '回转窑月累运转率'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='每月生产信息';
"""
vn.train(ddl=d1)

# vn.ask("2023年8月7日生产信息情况")
VannaFlaskApp(vn).run()


