#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2024/03/22 10:37:43
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

import os
import sys
# 根路径，设置在'data'目录下是避免某些服务器'/home'可用空间不足

WORK_DIR = sys.path[0]

# logs
os.makedirs(f"{WORK_DIR}/logs", exist_ok=True)
os.makedirs(f"{WORK_DIR}/logs/info", exist_ok=True)
os.makedirs(f"{WORK_DIR}/logs/error", exist_ok=True)
LOG_FILE = f"{WORK_DIR}/logs/log.jsonl"

# backend service
SERVER_PORT = 8080
