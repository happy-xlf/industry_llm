#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   chat_show.py
@Time    :   2024/03/25 18:33:50
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

import gradio as gr
import sys
from gradio.components import (
    Button,
    Chatbot,
    Component,
    Markdown,
    State,
    Textbox,
    get_component_instance,
)
sys.path.append("/Users/xiaofengzai/Desktop/industry_llm/")
# from backend.agent_api import chat
from backend.sql_agent import chat

if __name__ == "__main__":
    demo = gr.ChatInterface(chat, title="Chat with Industry-AI").queue()
    demo.launch(server_name="0.0.0.0", server_port=9999)