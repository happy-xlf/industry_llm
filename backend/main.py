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


class QueryRequest(BaseModel):
    text: str

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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/get_day/")
def get_day(message: QueryRequest):
    date = check_date(message.text)
    return JSONResponse(
        content=jsonable_encoder(get_day_api(date)),
    )

@app.post("/get_month/")
def get_month(message: QueryRequest):
    date = check_month_date(message.text)
    return JSONResponse(
        content=jsonable_encoder(get_month_api(date)),
    )

@app.post("/get_recenty/")
def get_recenty(message: QueryRequest):
    date = check_date(message.text)
    return JSONResponse(
        content=jsonable_encoder(get_recenty_api(date)),
    )

def api_start():
    uvicorn.run(app, host="0.0.0.0", port=SERVER_PORT)