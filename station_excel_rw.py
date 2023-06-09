# -*- coding: utf-8 -*-
# Written by xunjueyulin
# 2023-05-22
import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(__file__))
# 导入模块
from requests.exceptions import ReadTimeout, ConnectTimeout, RequestException
from address_translate import gdaddress_translate, gdcoordsys_translate

# 定义高德key
gdkey = "-"

# 读取文件，提前将需要转换的地址和经纬度处理好填入模板excel
station_filename = 'address_translation_template.xlsx'
station = pd.read_excel(station_filename, header=0)
# print(station["拼合经纬度"])
# 处理文件
station_location = station["拼合经纬度"]
gdaddress = []
try:
    for key in station_location:
        address_temp = gdaddress_translate(gdcoordsys_translate(key, 'gps', gdkey), gdkey)
        gdaddress.append(address_temp)
except:
    print("station translation error")


# 写入文件
# station_location = station.to_excel('filename', index=Flase)
# 将list对象转为dataframe
# gdaddress_df = pd.DataFrame(gdaddress)
# gdaddress_df.to_excel(station_filename, index=False, header="高德地址")
station_gd = pd.DataFrame(data=None)
station_gd["高德地址"] = gdaddress
# 拼接dataframe,axis=1为左右拼接
station_all = pd.concat([station, station_gd], axis=1)
# print(station_all)
station_all.to_excel(station_filename, index=False)
