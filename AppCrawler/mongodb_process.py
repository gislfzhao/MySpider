# -*- coding: utf-8 -*-
import pymongo
import json
import time

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['weixin']
collection = db['地球知识局']


def query_data():
    results = collection.find({})
    print(results, type(results))
    datas = []
    count = 0
    for result in results:
        del result['_id']
        result['datetime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(result.get('datetime')))
        if result.get('source_url') != '':
            count += 1
            result['index'] = count
            datas.append(result)
            print(result)
    return datas


def write_to_json(datas, filename='地球知识局.json'):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(json.dumps(datas, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    datas = query_data()
    write_to_json(datas)