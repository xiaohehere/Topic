# -*- coding: utf-8 -*-
import time
import json
import random

map_filename = "json/map.json"
chart_1_FILENAME = 'json/chart_1.json'
chart_2_FILENAME = 'json/chart_2.json'
chart_3_FILENAME = 'json/chart_3.json'
chart_4_FILENAME = 'json/chart_4.json'
chart_5_FILENAME = 'json/chart_5.json'
chart_6_FILENAME = 'json/chart_6.json'
table_1_FILENAME = 'json/table_1.json'

chart_map_lines_FILENAME = 'json/chart_map_lines.json'
chart_map_effectScatter_FILENAME = 'json/chart_map_effectScatter.json'

table_2_FILENAME = 'json/table_2.json'
table_3_FILENAME = 'json/table_3.json'




def read_config(config_file, section):
    with open(config_file, 'r', encoding="utf-8") as f:
        data = json.load(f)
        if section:
            return data[section]
        else:
            return data

def write_config(config_file, data):

    with open(config_file, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    f.close()