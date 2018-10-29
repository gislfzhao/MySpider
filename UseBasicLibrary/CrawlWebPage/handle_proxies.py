# -*- coding: utf-8 -*-
import json
import re


def read_from_txt(path):
    lit = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            dit = json.loads(line)
            text = parse_txt(dit)
            if text != "":
                lit.append(text)
    write_to_txt(lit)
    f.close()


def parse_txt(content):
    time = content["存活时间"]
    unit = re.sub('\d+', '', time)
    if unit == '天':
        value = int(re.sub('\D+', '', time))
        if value >= 10:
            lit = dict()
            lit[content["类型"].lower()] = content["类型"].lower() + "://" + content["IP地址"] + ":" + content["端口"]
            return lit
    return ""


def write_to_txt(text):
    with open('handle_proxies_result2.txt', 'a', encoding="utf-8") as f:
        f.write(json.dumps(text))
    # f.close()


def main():
    read_from_txt('proxies_result3.txt')


if __name__ == '__main__':
    main()
