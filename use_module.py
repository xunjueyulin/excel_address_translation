# -*- coding: utf-8 -*-
# Written by xunjueyulin
# 2023-05-19

# 读取excel文件
# 调用模块
# 写入返回结果
import os
import sys
import pandas as pd
# 将项目根目录添加到模块导入路径中
sys.path.append(os.path.dirname(__file__))
# 导入模块
from requests.exceptions import ReadTimeout, ConnectTimeout, RequestException
from address_translate import gdaddress_translate, gdcoordsys_translate

# 定义高德key
gdkey = "-"

# 引用模块示例
# test_address = address_translate(gdcoordsys_translate('113.271922,23.18349', 'gps', key), key)

# 读取excel表格
