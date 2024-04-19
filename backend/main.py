#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2024/03/21 16:40:39
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
import sys
import uvicorn
# sys.path.append("/Users/xiaofengzai/Desktop/industry_llm/")
from typing import Union
from backend.api.get_opc_api import get_day_api, get_month_api, get_recenty_api
from backend.api.get_opc_api import check_date, check_month_date
from config.settings import SERVER_PORT
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.chatglm import get_chatglm

chatglm, tokenizer = get_chatglm()

class QueryRequest(BaseModel):
    text: str

class QueryLikst(BaseModel):
    text: list[dict]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/chat/")
def get_day(message: QueryRequest):
    response, history = chatglm.chat(tokenizer, message.text, history=[])
    print(history)
    return JSONResponse(
        content=jsonable_encoder(response),
    )

@app.post("/multi_chat/")
def get_day(message: QueryLikst):
    message = message.text
    query = message[-1]['content']
    message.pop(-1)
    response, _ = chatglm.chat(tokenizer, query, history=message)
    return JSONResponse(
        content=jsonable_encoder(response),
    )

def api_start():
    uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT)