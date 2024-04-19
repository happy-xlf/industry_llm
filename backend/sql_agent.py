#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   sql_agent.py
@Time    :   2024/03/26 20:16:44
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

from langchain.llms import OpenAI
import os

from langchain.schema import HumanMessage
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

os.environ["OPENAI_PROXY"] = "http://127.0.0.1:7890"

db_user = "root"
db_password = "rootroot"
db_host = "localhost"
db_name = "industry"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

openai_api_key = os.environ["OPENAI_API_KEY"]

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, return_intermediate_steps=True)

# questions = "2023年5月1日的生产信息？"
# res = db_chain.run(questions)
# print("问题：", questions, "解答：", res)

# questions = "2023年5月1日的opc生料日产多少？"
# res = db_chain.run(questions)
# print("问题：", questions, "解答：", res)

# questions = "2023年5月7日附近几天的opc生料日产情况？"
# res = db_chain.run(questions)
# print("问题：", questions, "解答：", res)

# questions = "2023年5月总体生产情况？"
# res = db_chain.run(questions)
# print("问题：", questions, "解答：", res)

# questions = "2023年5月与6月生产信息比较？6月相对于5月的变化在哪里？"
# res = db_chain.run(questions)
# print("问题：", questions, "解答：", res)
import time

def chat(query, history: list[list[str]] = None):
    res = db_chain(query)

    sql_cmd = f"{res['intermediate_steps'][1]}"
    sql_result = f"{res['intermediate_steps'][3]}"
    answer = f"\n{res['result']}"

    response = ""
    for character in (sql_cmd,sql_result,answer):
        response += character + "\n"
        time.sleep(0.1)
        yield response

    return response


# questions = "2023年5月10日附近的src生料日产情况？分析最近的src生料日产趋势"
# res = db_chain(questions)

# sql_cmd = res['intermediate_steps'][1]
# sql_result = res['intermediate_steps'][3]
# answer = res['result']
# print("问题：", questions, "解答：", res)

