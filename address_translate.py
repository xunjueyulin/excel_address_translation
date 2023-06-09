# -*- coding: utf-8 -*-
# Written by xunjueyulin
# 2023-05-19

# 调取高德api示例
# https://restapi.amap.com/v3/geocode/geo?address=北京市朝阳区阜通东大街6号&output=XML&key=<用户的key>
# //restapi.amap.com/v3/geocode/geo?key=您的key&address=北京市朝阳区阜通东大街6号&city=北京

# 坐标转换api示例
# https://restapi.amap.com/v3/assistant/coordinate/convert?locations=116.481499,39.990475&coordsys=gps&output=xml&key=<用户的key>
# //restapi.amap.com/v3/assistant/coordinate/convert?locations=116.481499,39.990475&coordsys=gps&key=<用户的key>


# 导入库
import requests
from requests.exceptions import ReadTimeout, ConnectTimeout, RequestException

# 构造坐标转高德地址函数,传入经纬度和key


def gdaddress_translate(gdlocation, key):
    # 定义参数，包括高德坐标（经纬度小数点后不要超过 6 位）、key
    parameters = {'location': gdlocation, 'key': key, 'extensions': 'base', 'batch': 'false', 'roadlevel': 0,
                  'radius': 0, 'poitype': ''}
    # 定义api链接地址
    base = 'https://restapi.amap.com/v3/geocode/regeo'
    # 定义转换后的高德地址字段
    address_gd = ""
    try:
        # 发生get请求，设置2秒停止响应
        response = requests.get(base, parameters, timeout=2)
        if response.status_code == 200:
            # 如请求成功，对返回的json进行解析
            answer = response.json()
            # print(answer)
            # 取回高德地址
            address_gd = answer["regeocode"]["formatted_address"]
        else:
            # 请求失败，返回失败的坐标和网络状态码
            print(str(gdlocation) + "address translate error，status_code=" + str(response.status_code))
            pass
    # 捕获错误
    except ReadTimeout:
        print("Server read timeout")
    except ConnectTimeout:
        print("Server connect timeout")
    except RequestException:
        print("Server request failure")
    # 返回高德地址
    return address_gd
# 注释WGS84坐标系地址转换高德坐标系


def gdcoordsys_translate(locations, coordsys, key):
    # 定义参数，包括坐标、原坐标系、key
    parameters = {'locations':locations, 'coordsys':coordsys, 'key':key}
    # 定义api链接地址
    base = 'https://restapi.amap.com/v3/assistant/coordinate/convert'
    # 定义转换后的高德坐标字段
    locations_gd = 0
    try:
        # 发生get请求，设置2秒停止响应
        response = requests.get(base, parameters, timeout=2)
        if response.status_code == 200:
            # 如请求成功，对返回的json进行解析
            answer = response.json()
            # print(answer)
            # 取回高德坐标
            locations_gd = answer["locations"]
        else:
            # 请求失败，返回失败的坐标和网络状态码
            print(str(locations) + "coordsys translate error，status_code=" + str(response.status_code))
            pass
    # 捕获错误
    except ReadTimeout:
        print("Server read timeout")
    except ConnectTimeout:
        print("Server connect timeout")
    except RequestException:
        print("Server request failure")
    # 返回高德坐标
    return locations_gd


key = "-"
# test_location = gdcoordsys_translate('113.563304,22.746745', 'gps', key)
# test_address = gdaddress_translate(test_location, key)
# test_address = address_translate(gdcoordsys_translate('113.271922,23.18349', 'gps', key), key)
# test_address = address_translate('113.568397,22.743756', key)
# print(test_address)
