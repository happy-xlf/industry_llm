#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   opc_src_entity.py
@Time    :   2024/03/21 16:52:13
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class OPC_SRC():
    def __init__(self, data):
        self.message = data

    def get_data(self):
        return self.message