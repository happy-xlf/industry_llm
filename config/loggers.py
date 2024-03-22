#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   loggers.py
@Time    :   2024/03/22 10:37:19
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

import logging.handlers

from config.settings import WORK_DIR

# 初始化logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

# info file handler
info_handler = logging.handlers.TimedRotatingFileHandler(
    filename=f"{WORK_DIR}/logs/info/run.log", when='midnight', delay=True
)
# 日志格式为"[{level}] {time} - {file_name} - {mesage}"
info_handler.setFormatter(logging.Formatter(
    '[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))
info_handler.setLevel(logging.INFO)

# error file handler
error_handler = logging.handlers.TimedRotatingFileHandler(
    filename=f"{WORK_DIR}/logs/error/errors.log", when='midnight', delay=True
)
error_handler.setFormatter(logging.Formatter(
    '[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))
error_handler.setLevel(logging.ERROR)

# add handler
logger.addHandler(info_handler)
logger.addHandler(error_handler)
