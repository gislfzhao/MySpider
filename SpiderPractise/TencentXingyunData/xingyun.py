# -*- coding: utf-8 -*-
import requests
import json
import os.path


def get_xingyun_points(count=4, rank=0):
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
        "count": count,
        "rank": rank
    }
    try:
        # 对于post请求中的request payload形式，需要用json.dumps
        response = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException as e:
        print("ERROR:", e.args)
        return None


def parse_json(json_data):
    time = json_data.get('time')
    locs = json_data.get('locs').split(',')
    for i in range(len(locs)//3):
        lat = int(locs[0+3*i])/100
        long = int(locs[1+3*i])/100
        count = locs[2+3*i]
        print('{},{},{},{}'.format(time, long, lat, count))
        write_to_txt(time, content='{},{},{},{}'.format(time, long, lat, count))


def write_to_txt(filename, content):
    filename = filename.replace(':', '：') + " XingyunPoints.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('time,longitude,latitude,count\n')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content+'\n')


def main():
    json_points = get_xingyun_points(4, 0)
    parse_json(json_points)
    pass


if __name__ == '__main__':
    main()
