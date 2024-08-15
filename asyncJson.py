# -*- coding: utf-8 -*-
from config import *


def change_chart_1():
    print("change chart 1 ")
    datas = read_config(map_filename, "")

    start = 0
    end = start + 300
    # data = read_config(chart_1_FILENAME,"")
    length = len(datas)
    print("数组长度", length)
    l = []
    rs = []
    i = 0

    while i < length:
        node = {}
        node["name"] = datas[i][2]
        j = 0
        while j < 9:
            v = random.randint(start, end)
            l.append(v)
            j = j+1
        node["data"] = l
        i = i + 1
        rs.append(node)

    write_config(chart_1_FILENAME, rs)


def change_chart_2():
    print("change_chart_2")

    start = 1
    end = 2000
    datas = read_config(chart_2_FILENAME, "")
    l = []
    i = 0
    while i < 6:
        v = random.randint(start, end)
        l.append(v)
        i = i + 1

    write_config(chart_2_FILENAME, l)


def change_chart_3():
    print("change plc")
    start = 1
    end = 2000
    datas = read_config(chart_3_FILENAME, "")
    for v in datas:
        v["value"] = random.randint(start, end)

    write_config(chart_3_FILENAME, datas)


def change_chart_map():
    mapCoords = [
        [
            118.094546,
            24.457543,
            "厦门大学附属第一医院",
            13,
            33,
            44,
            "福建省厦门市思明区镇海路55号"],
        [
            118.094564,
            24.457358,
            "厦门第一医院",
            28,
            53,
            64,
            "xxx"],
        [
            118.053898,
            24.566955,
            "厦门大学附属第一医院杏林医院",
            38,
            43,
            24,
            "厦门市集美区杏林洪埭路11号"],
        [
            118.14748,
            24.506295,
            "厦门中医院",
            18,
            93,
            74,
            "福建省厦门市仙岳路1739号"],
        [
            118.11087,
            24.590336,
            "厦门医学院附属第二医院",
            8,
            3,
            4,
            "厦门市集美区盛光路566号"]]

    print("change_chart_map", map_filename)
    mapCoordsLen = len(mapCoords) - 1
    datas = read_config(map_filename, "")
    i = random.randint(0, mapCoordsLen)
    j = random.randint(0, mapCoordsLen)
    k = random.randint(0, mapCoordsLen)

    datas = [mapCoords[i], mapCoords[j], mapCoords[k]]

    write_config(map_filename, datas)


def change_chart_4():
    print("change 设备在线情况")
    start = 10
    end = 100
    datas = read_config(chart_4_FILENAME, "")
    for node in datas:
        node["value"] = random.randint(start, end)
        # 递增效果
        start = start + 100
        end = end + 100
    write_config(chart_4_FILENAME, datas)


def change_chart_5():
    print("change 工场数据")
    start = 10
    end = 100
    datas = read_config(chart_5_FILENAME, "")
    for node in datas:
        node["value"] = random.randint(start, end)
    write_config(chart_5_FILENAME, datas)


def change_chart_6():
    print("change 点柱图")
    start = 100
    end = 500
    datas = read_config(chart_6_FILENAME, "")
    i = 0
    while i < 20:
        datas["alm"][i] = random.randint(start, end)
        datas["msg"][i] = random.randint(start, end)
        i = i + 1
    write_config(chart_6_FILENAME, datas)


def change_table_1():
    print("change", table_1_FILENAME)

    datas = ["2019年5月4日市A区12#机器气压过高报警",
             "上海市A区12#机器气压过高报警",
             "江苏省12#机器气压过高报警",
             "河南省郑州市B区12#机器气压过高报警",
             "湖北省12#机器气压过高报警",
             "海南省B区12#机器气压过高报警",
             "北京市A区12#机器气压过高报警",
             "东北省吉林市12#机器气压过高报警",
             "山西省大同市B区12#机器气压过高报警",
             "山东省12#机器气压过高报警",
             "广西省桂林市B区12#机器气压过高报警"
             ]
    start = 0
    end = len(datas) - 1

    i = random.randint(start, end)
    j = random.randint(start, end)
    k = random.randint(start, end)

    data = read_config(table_1_FILENAME, "")
    i = 0
    while i < 3:
        node = {"msg": datas[random.randint(start, end)]}
        data[i] = node
        i = i+1
    write_config(table_1_FILENAME, data)


def change_table_2():
    print("change", table_2_FILENAME)
    datas = read_config(table_2_FILENAME, "")
    start = 100
    end = 1000
    # company
    for node in datas:
        node["dtuCnt"] = random.randint(start, end)
        node["plcCnt"] = random.randint(start, end)
        node["dataCnt"] = random.randint(start, end)

    write_config(table_2_FILENAME, datas)


def change_all_json():
    # 地图
    change_chart_map()
    # line1
    change_chart_1()
    # 6 个数值
    change_chart_2()
    # # plc
    # change_chart_3()
    # # 设备在线情况
    # change_chart_4()
    # change_chart_5()
    # change_chart_6()
    #
    # change_table_1()
    # change_table_2()


def loop():
    while 1:
        change_all_json()
        time.sleep(1)


if __name__ == "__main__":
    loop()
