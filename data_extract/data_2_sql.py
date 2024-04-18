#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   data_2_sql.py
@Time    :   2024/04/10 18:38:17
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
import os, re


def get_all_text(data_dir):
    file_list = os.listdir(data_dir)
    return [os.path.join(data_dir, file) for file in file_list]

def get_num(it):
    numbers = re.findall(r'\d+\.?\d*', it)
    return float(numbers[0]), float(numbers[1]), numbers[2]+str("%")

def check_date(message):
    pattern = r'(\d{4}年\d{1,2}月\d{1,2}日)'
    pattern = re.compile(pattern)
    result = pattern.findall(message)[0]
    year = check_year(result)
    month = check_month(result)
    day = check_day(result)
    return f"{year}-{month}-{day}"

def check_month_date(message):
    pattern = r'(\d{4}年\d{1,2}月\d{1,2}日)'
    pattern = re.compile(pattern)
    result = pattern.findall(message)[0]
    year = check_year(result)
    month = check_month(result)

    return f"{year}-{month}"

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

def save_day_data(file_dir):
    with open(file_dir, 'r', encoding='utf-8') as f:
        data = f.readlines()
    date_list = []
    opc_raw = []
    src_raw = []
    mo_lv = []
    opc = []
    src = []
    hui_lv = []
    zhu = []

    month = []
    month_opc_raw = []
    month_src_raw = []
    month_mo_lv = []
    month_opc = []
    month_src = []
    month_hui_lv = []
    idx = 0
    while idx < len(data):
        it = data[idx]
        if "生产信息" in it:
            it=it.replace("生产信息","")
            date_list.append(check_date(it.strip()))
            idx+=1

            it = data[idx]
            opc_it, src_it, mo_lv_it = get_num(it)
            opc_raw.append(opc_it)
            src_raw.append(src_it)
            mo_lv.append(mo_lv_it)
            idx+=1

            it = data[idx]
            opc_it, src_it, hui_lv_it = get_num(it)
            opc.append(opc_it)
            src.append(src_it)
            hui_lv.append(hui_lv_it)
            idx+=1

            it = data[idx]
            if "生产信息" in it or "截止" in it:
                zhu.append("")
                
            else:
                res= []
                while idx < len(data):
                    it = data[idx]
                    
                    if "生产信息" in it or "截止" in it:    
                        break
                    else:
                        res.append(it.strip())
                        idx+=1
                zhu_temp = "\n".join(res)
                zhu.append(zhu_temp)
        elif "截止" in it:
            it=it.replace("截止","")
            month.append(check_month_date(it.strip()))
            idx+=1

            it = data[idx]
            opc_it, src_it, mo_lv_it = get_num(it)
            month_opc_raw.append(opc_it)
            month_src_raw.append(src_it)
            month_mo_lv.append(mo_lv_it)
            idx+=1
            
            opc_it, src_it, hui_lv_it = get_num(it)
            month_opc.append(opc_it)
            month_src.append(src_it)
            month_hui_lv.append(hui_lv_it)
            break

    import pymysql
    # 打开数据库连接
    conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="rootroot",db="industry")
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()

    # 插入数据到day_message表中
    for i in range(len(date_list)):
        print(date_list[i], opc_raw[i], src_raw[i], mo_lv[i], opc[i], src[i], hui_lv[i], zhu[i])
        print("----------------------------------")
        sql = "insert into day_message values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (date_list[i], opc_raw[i], src_raw[i], mo_lv[i], opc[i], src[i], hui_lv[i], zhu[i]))

        conn.commit()
    
    for i in range(len(month)):
        print(month[i], month_opc_raw[i], month_src_raw[i], month_mo_lv[i], month_opc[i], month_src[i], month_hui_lv[i])
        print("----------------------------------")
        sql = "insert into month_message values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (month[i], month_opc_raw[i], month_src_raw[i], month_mo_lv[i], month_opc[i], month_src[i], month_hui_lv[i]))
        conn.commit()
    conn.close()
    cursor.close()

if __name__ == '__main__':
    data_dir = "./message_data/"
    file_list = get_all_text(data_dir)
    file_list.sort()
    print(file_list)
    for file in file_list:
        save_day_data(file)
       
