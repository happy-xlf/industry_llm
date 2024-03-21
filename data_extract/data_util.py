#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   data_util.py
@Time    :   2024/03/17 21:38:21
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

import pandas as pd
import os

def str_date(data):
    return str(data).strip()

def check_num(num):
    if num == "":
        return 0
    else:
        return str(num).strip()

def get_data_two(data):
    ans = []
    i = 2
    flag = -19999999
    
    while i < len(data):
        all_data = data[i].split(",")
        if i==2:
            time_date = str_date(all_data[0]) + str_date(all_data[1]) + str_date(all_data[2]) + str_date(all_data[3]) + str_date(all_data[4])
            if "2023年8月4日" in time_date:
                print(time_date)
            ans.append(time_date + "生产信息")
            print(time_date)
        elif i==4:
            factor = all_data[0]
            factor_day = check_num(all_data[5])

            opc = all_data[1]
            opc_day= check_num(all_data[2])
            beizhu_1 = all_data[8]
        elif i==5:
            beizhu_2 = all_data[0]
            beizhu = beizhu_1 + beizhu_2
            while data[i+1].split(",")[0] != "":
                beizhu += data[i+1].split(",")[0]
                i=i+1
            flag = i
        elif i==flag+1:
            src = all_data[1]
            src_num = check_num(all_data[2])
            ans.append(f"{opc}日产{opc_day}吨，{src}日产{src_num}吨, {factor}日运转率{factor_day}")
            print(f"{opc}日产{opc_day}吨，{src}日产{src_num}吨, {factor}日运转率{factor_day}")
        elif i==flag+2:
            hui = all_data[0]
            hui_day = check_num(all_data[5])
            opc_s = all_data[1]
            opc_s_day = check_num(all_data[2])
        elif i==flag+3:
            src_s = all_data[1]
            src_s_sum = check_num(all_data[2])
            ans.append(f"{opc_s}日产{opc_s_day}吨，{src_s}日产{src_s_sum}吨, {hui}日运转率{hui_day}")
            beizhu = str(beizhu).replace("\"", "").rstrip()
            ans.append(f"{beizhu}")
            print(f"{opc_s}日产{opc_s_day}吨，{src_s}日产{src_s_sum}吨, {hui}日运转率{hui_day}")
            print(f"{beizhu}")
            break
        i+=1
    return ans

def get_data_one(data):
    ans = []
    for i in range(2,len(data)):
        all_data = data[i].split(",")
        if i==2:
            time_date = str_date(all_data[0]) + str_date(all_data[1]) + str_date(all_data[2]) + str_date(all_data[3]) + str_date(all_data[4])
            ans.append(time_date + "生产信息")
            print(time_date)
        elif i==4:
            factor = all_data[0]
            factor_day = check_num(all_data[5])

            opc = all_data[1]
            opc_day= check_num(all_data[2])
            beizhu = all_data[8]
        elif i==5:
            src = all_data[1]
            src_num = check_num(all_data[2])
        elif i==6:
            ans.append(f"{opc}日产{opc_day}吨，{src}日产{src_num}吨, {factor}日运转率{factor_day}")
            print(f"{opc}日产{opc_day}吨，{src}日产{src_num}吨, {factor}日运转率{factor_day}")
            hui = all_data[0]
            hui_day = check_num(all_data[5])
            opc_s = all_data[1]
            opc_s_day = check_num(all_data[2])
        elif i==7:
            src_s = all_data[1]
            src_s_sum = check_num(all_data[2])
            ans.append(f"{opc_s}日产{opc_s_day}吨，{src_s}日产{src_s_sum}吨, {hui}日运转率{hui_day}")
            if beizhu!="" and beizhu!="\n":
                beizhu = str(beizhu).replace("\"", "").rstrip()
                ans.append(f"{beizhu}")
            print(f"{opc_s}日产{opc_s_day}吨，{src_s}日产{src_s_sum}吨, {hui}日运转率{hui_day}")
            print(f"{beizhu}")
            break
    return ans

def get_data(data):
    all_data = data[5].split(",")
    if all_data[0]!="":
        res = get_data_two(data)
    else:
        res = get_data_one(data)
    return res

def get_final_summary(data):
    res = []

    all_data = data[2].split(",")
    time_date = str_date(all_data[0]) + str_date(all_data[1]) + str_date(all_data[2]) + str_date(all_data[3]) + str_date(all_data[4])
    res.append("截止" + time_date)
    print("截止" + time_date)

    all_data = data[4].split(",")
    
    factor = all_data[0]
    factor_month = check_num(all_data[6])
    
    opc = all_data[1]
    opc_month= check_num(all_data[3])

    if data[5].split(",")[0] == "":
        all_data = data[5].split(",")
        src = all_data[1]
        src_month = check_num(all_data[3])
        print(f"{opc}月产{opc_month}吨，{src}月产{src_month}吨, {factor}月累运转率{factor_month}")
        res.append(f"{opc}月产{opc_month}吨，{src}月产{src_month}吨, {factor}月累运转率{factor_month}")
        
        all_data = data[6].split(",")
        hui = all_data[0]
        hui_month = check_num(all_data[6])
        opc_s = all_data[1]
        opc_s_month = check_num(all_data[3])

        all_data = data[7].split(",")
        src_s = all_data[1]
        src_s_month = check_num(all_data[3])
        print(f"{opc_s}月产{opc_s_month}吨，{src_s}月产{src_s_month}吨, {hui}月累运转率{hui_month}")
        res.append(f"{opc_s}月产{opc_s_month}吨，{src_s}月产{src_s_month}吨, {hui}月累运转率{hui_month}")
    else:
        i = 5
        while data[i+1].split(",")[0] != "":
            i=i+1
        flag = i
        all_data = data[flag+1].split(",")
        src = all_data[1]
        src_month = check_num(all_data[3])
        print(f"{opc}月产{opc_month}吨，{src}月产{src_month}吨, {factor}月累运转率{factor_month}")
        res.append(f"{opc}月产{opc_month}吨，{src}月产{src_month}吨, {factor}月累运转率{factor_month}")
        
        all_data = data[flag+2].split(",")
        hui = all_data[0]
        hui_month = check_num(all_data[6])
        opc_s = all_data[1]
        opc_s_month = check_num(all_data[3])

        all_data = data[flag+3].split(",")
        src_s = all_data[1]
        src_s_month = check_num(all_data[3])
        print(f"{opc_s}月产{opc_s_month}吨，{src_s}月产{src_s_month}吨, {hui}月累运转率{hui_month}")
        res.append(f"{opc_s}月产{opc_s_month}吨，{src_s}月产{src_s_month}吨, {hui}月累运转率{hui_month}")
    
    return res




if __name__ == '__main__':
    folder_path = "./data/"
    all_files = os.listdir(folder_path)
    for file in all_files:
        print("***********"+file+"*************")
        with open(folder_path+file, "r", encoding="utf-8") as f:
            data = f.readlines()
        lun = 8
        lens = len(data)

        begin = 0
        ans = []
        tag = "项目生产信息"
        indexs = [i for i, x in enumerate(data) if tag in str(x)]
        end = 0
        for i in range(1,len(indexs)):
            begin = indexs[i-1]
            end = indexs[i]
            res = get_data(data[begin:end])
            ans.extend(res)
        res = get_data(data[end:lens])
        ans.extend(res)

        final_summary = get_final_summary(data[end:lens])
        ans.extend(final_summary)
        
        print(len(ans))
        res_file = file.split(".")[0]+".txt"
        with open("./message_data/"+res_file, "w", encoding="utf-8") as f:
            for it in ans:
                f.write(it)
                f.write("\n")


