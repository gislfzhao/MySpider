# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import time
from multiprocessing import Pool


def get_TecentData(rank=0):  # 先默认为从rank从0开始
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '20',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Host': 'xingyun.map.qq.com',
        'Origin': 'https://xingyun.map.qq.com',
        'Referer': 'https://xingyun.map.qq.com/index.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36 '
    }
    url = "https://xingyun.map.qq.com/api/getXingyunPoints"
    data = {
        "count": 4,
        "rank": rank
    }
    response = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=30)
    dictdatas = response.json()
    time = dictdatas["time"]  # 有了dict格式就可以根据关键字提取数据了，先提取时间
    print(time)
    locs = dictdatas["locs"]  # 再提取locs（这个需要进一步分析提取出经纬度和定位次数）
    locss = locs.split(",")
    # newloc=[locss[i:i+3] for i in range(0,len(locss),3)]
    temp = []  # 搞一个容器
    for i in range(int(len(locss) / 3)):
        lat = locss[0 + 3 * i]  # 得到纬度
        lon = locss[1 + 3 * i]  # 得到经度
        count = locss[2 + 3 * i]

        temp.append([time, int(lat) / 100, int(lon) / 100, count])  # 容器追加四个字段的数据：时间，纬度，经度和定位次数

    result = pd.DataFrame(temp)  # 用到神器pandas，真好用
    result.dropna()  # 去掉脏数据，相当于数据过滤了
    result.columns = ['time', 'lat', 'lon', 'count']
    result.to_csv('TecentDataRank'+str(rank)+'.txt', mode='a', index=False)  # model="a",a的意思就是append，可以把得到的数据一直往TecentData.txt中追加


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_TecentData, range(4))
    pool.close()
    pool.join()


