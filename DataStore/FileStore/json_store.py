# -*- coding: utf-8 -*-
import json

str = '''
[{
"name": "Bob",
"gender": "male",
"birthday": "1992-10-18"
}, {
"name": "Selina",
"gender": "female",
"birthday": "1995-10-18"
}]
'''
# print(type(str), str)
# data = json.loads(str)
# print(type(data), data)
# print(data[0]['name'])


def read_from_json():
    with open('data.json', 'r') as f:
        st = f.read()
        data = json.loads(st)
        print(data)


def output_to_json():
    with open('data2.json', 'w') as f:
        data = [{
            "name": "Sellia",
            "gender": "female",
            "birthday": "1995-10-18"
        }]
        f.write(json.dumps(data, indent=2))


def output_to_json2():
    with open('data3.json', 'w', encoding='utf-8') as f:
        data = [{
            "name": "汪峰",
            "gender": "男",
            "birthday": "1975-10-18"
        }]
        f.write(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    output_to_json2()
    pass
