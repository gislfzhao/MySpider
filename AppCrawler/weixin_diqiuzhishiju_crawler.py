# -*- coding: utf-8 -*-
from mitmproxy import ctx
import re
import pymongo
import json


def response(flow):
    print('开始入库：')
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['weixin']
    collection = db['地球知识局']
    info = ctx.log.info     # info输出时必须以字符串形式
    url_home = 'https://mp.weixin.qq.com/mp/profile_ext?action=home'
    url_msg = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg'
    if flow.request.url.startswith(url_home):
        text = flow.response.text
        msg_re = re.compile(".*?var msgList = '(.*?)';.*?", re.S)
        msg_lists = msg_re.search(text).group(1).replace('&quot;', '"')
        msg_lists2 = json.loads(msg_lists)
        process_msg_lists(collection, msg_lists2)

    elif flow.request.url.startswith(url_msg):
        text = flow.response.text
        text = text.replace('\n', '').replace('"{', '{').replace('}"', '}').replace('\\', '')
        data = json.loads(text)
        msg_lists = data.get('general_msg_list')
        process_msg_lists(collection, msg_lists)


def process_msg_lists(collection, msg_lists):
    for msg in msg_lists.get('list'):
        id = msg.get('comm_msg_info').get('id')
        datetime = msg.get('comm_msg_info').get('datetime')
        fakeid = msg.get('comm_msg_info').get('fakeid')

        title = msg.get('app_msg_ext_info').get('title')
        digest = msg.get('app_msg_ext_info').get('digest')
        content_url = msg.get('app_msg_ext_info').get('content_url')
        source_url = msg.get('app_msg_ext_info').get('source_url')
        cover = msg.get('app_msg_ext_info').get('cover')
        author = msg.get('app_msg_ext_info').get('author')
        copyright_stat = msg.get('app_msg_ext_info').get('copyright_stat')

        result = {
            'title': title,
            'digest': digest,
            'content_url': content_url.replace('\\', ''),
            'source_url': source_url.replace('\\', ''),
            'cover': cover.replace('\\', ''),
            'author': author,
            'copyright_stat': copyright_stat,
            'id': id,
            'datetime': datetime,
            'fakeid': fakeid
        }
        collection.insert_one(result)
        ctx.log.info('插入数据：' + str(result)[:80])

        if msg.get('app_msg_ext_info').get('is_multi') == 1:
            for item in msg.get('app_msg_ext_info').get('multi_app_msg_item_list'):
                title = item.get('title')
                digest = item.get('digest')
                content_url = item.get('content_url')
                source_url = item.get('source_url')
                cover = item.get('cover')
                author = item.get('author')
                copyright_stat = item.get('copyright_stat')

                result = {
                    'title': title,
                    'digest': digest,
                    'content_url': content_url.replace('\\', ''),
                    'source_url': source_url.replace('\\', ''),
                    'cover': cover.replace('\\', ''),
                    'author': author,
                    'copyright_stat': copyright_stat,
                    'id': id,
                    'datetime': datetime,
                    'fakeid': fakeid
                }
                collection.insert_one(result)
                ctx.log.info('插入数据：' + str(result)[:80])
