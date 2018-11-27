# -*- coding: utf-8 -*-
from mitmproxy import ctx
import pymongo
import json


def response(flow):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['igetget']
    collection = db['books']
    url = 'http://ah2.zhangyue.com/zybk/api/rank/books'
    info = ctx.log.info
    # startswith() 方法用于检查字符串是否是以指定子字符串开头
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        # info(str(data))
        books = data.get('body')
        print("数目:" + str(len(books)))
        for book in books:
            # info(str(book))
            data = {
                'name': book.get('name'),
                'author': book.get('author'),
                'bookRating': book.get('bookRating'),
                'category':  book.get('category'),
                'desc': book.get('desc'),
                'url': book.get('url'),
                'id': book.get('id'),
                'pic': book.get('pic')
            }
            # print('数据')
            info(str(data))
            collection.insert_one(data)

