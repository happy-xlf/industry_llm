#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   get_day.py
@Time    :   2024/03/21 16:58:53
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

import os
from backend.entity.opc_src_entity import OPC_SRC
from backend.entity.opc_src_month import OPC_SRC_Month
import re
from config.settings import WORK_DIR


def get_day_api(date):
    data: OPC_SRC=all_day[date]
    return data.get_data()

def get_month_api(date):
    data: OPC_SRC_Month=all_month[date]
    return data.get_data()

def get_recenty_api(date):
    # 返回最近五天的数据
    day = int(date[-2:])
    dates = []
    if day <= 5:
        dates = [f"{date[:-2]}0{i}" for i in range(1, day+1)]
    else:
        for i in range(day-4, day+1):
            if i < 10:
                dates.append(f"{date[:-2]}0{i}")
            else:
                dates.append(f"{date[:-2]}{i}")
    data = [get_day_api(date) for date in dates]
    return data

def check_date(message):
    pattern = r'(\d{4}年\d{1,2}月\d{1,2}日)'
    pattern = re.compile(pattern)
    result = pattern.findall(message)[0]
    year = check_year(result)
    month = check_month(result)
    day = check_day(result)
    return year + month + day

def check_month_date(message):
    pattern = r'(\d{4}年\d{1,2}月)'
    pattern = re.compile(pattern)
    result = pattern.findall(message)[0]
    year = check_year(result)
    month = check_month(result)
    return year + month

def check_month(date):
    pattern = r'(\d{1,2}月)'
    pattern = re.compile(pattern)
    result = pattern.findall(date)[0][:-1]
    if len(result) == 1:
        return "0" + result
    else:
        return result

def check_day(date):
    pattern = r'(\d{1,2}日)'
    pattern = re.compile(pattern)
    result = pattern.findall(date)[0][:-1]
    if len(result) == 1:
        return "0" + result
    else:
        return result
    
def check_year(date):
    pattern = r'(\d{4}年)'
    pattern = re.compile(pattern)
    result = pattern.findall(date)[0][:-1]

    return result


    
path = os.path.join(WORK_DIR, "data_extract/message_data/")
file_list = os.listdir(path)

all_day = {}
all_month = {}
for name in file_list:
    with open(path + name, "r", encoding="utf-8") as f:
            data = f.readlines()
    i=0
    lens = len(data)
    while i < lens:
        if i < lens and "生产信息" in data[i]:
            message = data[i]
            result = check_date(message)
            i+=1
            while i < lens and "生产信息" not in data[i] and "截止" not in data[i]:
                message += data[i]
                i+=1
            if result not in all_day.keys():
                all_day[result] = OPC_SRC(message)
        if "截止" in data[i]:
            message = data[i]
            result = check_month_date(message)
            i+=1
            while i<lens and "截止" not in data[i]:
                message += data[i]
                i+=1
            if result not in all_month.keys():
                all_month[result] = OPC_SRC_Month(message)

