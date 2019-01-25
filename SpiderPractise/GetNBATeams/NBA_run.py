# -*- coding: utf-8 -*-
import requests
import os
import time
import re
import json
import pymongo
from multiprocessing import Pool
from urllib.parse import urlencode
from SpiderPractise.GetNBATeams.config import get_user_agent

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['igetget']
collection = db['NBA']


def get_teams_from_page():
    url = 'http://matchweb.sports.qq.com/rank/team?'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'matchweb.sports.qq.com',
        'Referer': 'http://nba.stats.qq.com/team/list.htm',
        'User-Agent': get_user_agent()
    }
    params = {
        'competitionId': '100000',
        'from': 'NBA_PC',
        'callback': 'jQuery1124021062478088276326_' + str(int(time.time() * 1000)),
        '_': int(time.time() * 1000)
    }
    try:
        response = requests.get(url + urlencode(params), headers=headers, timeout=10)
        if response.status_code == 200:
            text = response.text.encode('utf-8').decode("unicode_escape")
            text_re = re.compile('.*?\((.*?)\).*?', re.S)
            text = re.search(text_re, text).group(1)
            print(json.loads(text)[1])
            return json.loads(text)[1]
        else:
            print("None")
            return None
    except Exception as e:
        print("ERROR:", e.args)
        return None


def parse_teams_json(text):
    del text['east'], text['west']
    for key, value in text.items():
        if key in ['atlantic', 'central', 'eastsouth']:
            for team in value:
                result = {
                    'conference': 'East',
                    'division': key,
                    'name': team.get('name'),
                    'enName': team.get('enName'),
                    'logoNew': team.get('logoNew'),
                    'teamId': team.get('teamId')
                }
                # print(result)
                yield result
        elif key in ['pacific', 'westnorth', 'westsouth']:
            for team in value:
                result = {
                    'conference': 'West',
                    'division': key,
                    'name': team.get('name'),
                    'enName': team.get('enName'),
                    'logoNew': team.get('logoNew'),
                    'teamId': team.get('teamId')
                }
                # print(result)
                yield result


def save_team_logo(team):
    print('写入数据{}至MongoDB'.format(str(team)))
    collection.insert_one(team)

    if not os.path.exists('NBA'):
        os.mkdir('NBA')

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'Referer': 'http://nba.stats.qq.com/team/list.htm',
        'User-Agent': get_user_agent()
    }
    try:
        response = requests.get(team.get('logoNew'), headers=headers, timeout=12)
        if response.status_code == 200:
            filename = 'NBA/{}.png'.format(team.get('name'))
            if not os.path.exists(filename):
                with open(filename, 'wb') as f:
                    print('Downloading:', filename)
                    f.write(response.content)
            else:
                print('Already Downloaded', filename)
    except requests.ConnectionError:
        print('Failed to Save Image')
    except Exception as e:
        print("ERROR:", e.args)


def main():
    texts = get_teams_from_page()
    teams = parse_teams_json(texts)
    pool = Pool()
    pool.map(save_team_logo, teams)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
