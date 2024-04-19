#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   chatglm.py
@Time    :   2024/04/18 20:37:13
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

import os
import json

from transformers import AutoTokenizer, AutoModel

def get_chatglm():
    # system params
    os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    model_dir = "/home/lifeng/LLM_work/Models/ZhipuAI/chatglm3-6b"
    tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
    model.eval()
    return model, tokenizer