#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   agent_api.py
@Time    :   2024/03/25 16:48:34
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
import sys, os
sys.path.append("/Users/xiaofengzai/Desktop/industry_llm/backend")
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from send_api import get_post, get_month_api
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory
                                                  )
from langchain.agents.agent import AgentExecutor

os.environ["OPENAI_PROXY"] = "http://127.0.0.1:7890"
llm = OpenAI(temperature=0.3)
tools = [
    Tool(
        name = "获取某个日期附近的生产信息",
        func=get_post,
        description="当你需要获取某个日期附近的生产信息时很有用。该工具的输入是一个日期类型的信息。例如：2023年7月8日，这就是输入"
    ),
    Tool(
        name = "获取月份总体生产信息",
        func=get_month_api,
        description="当你需要获取月份总体生产信息时很有用。该工具的输入是一个日期类型的信息。例如：2023年7月，这就是输入"
    )
]
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True) 
agent: AgentExecutor = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# agent = initialize_agent(  
#     tools,  
#     llm,  
#     agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,  
#     verbose=True,  
#     memory=memory  
# )  

def chat(query: str, history: list[list[str]] = None):
    # print(response["intermediate_steps"])
    # 生成回复
    context = agent.run(query)
    return context
