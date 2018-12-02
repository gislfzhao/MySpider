# -*- coding: utf-8 -*-
import json
import pymongo
import re
from urllib.parse import unquote


def response(flow):
    client = pymongo.MongoClient('localhost')
    db = client['jd']
    comments_collection = db['comments']
    products_collection = db['products']

    # 提取商品数据
    url = 'cdnware.m.jd.com'
    if url in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        if data.get('wareInfo') and data.get('wareInfo').get('basicInfo'):
            info = data.get('wareInfo').get('basicInfo')
            id = info.get('wareId')
            name = info.get('name')
            images = info.get('wareImage')
            result = {
                'id': id,
                'name': name,
                'images': images
            }
            print(id, name, images)
            products_collection.update_one({
                'id': id,
                'name': name,
                'images': images
            }, {'$set': result}, upsert=True)

    # 提取评论数据
    url = 'api.m.jd.com/client.action?functionId=getCommentListWithCard'
    if url in flow.request.url:
        pattern = re.compile('sku\":\"(\d+)\"', re.S)
        # Request请求中包含商品的ID
        body = unquote(flow.request.text)
        # 提取商品的ID
        id = re.search(pattern, body).group(1) if re.search(pattern, body) else None
        # 提取Response
        text = flow.response.text
        data = json.loads(text)
        # 采用or逻辑运算符，若data中能get到值，则返回，否则返回空列表
        comments = data.get('commentInfoList') or list()
        # 提取评论数据
        for comment in comments:
            if comment.get('commentInfo') and comment.get('commentInfo').get('commentData'):
                info = comment.get('commentInfo')
                content = info.get('commentData')
                date = info.get('commentDate')
                score = info.get('commentScore')
                user_nickname = info.get('userNickName')
                product_attrs = info.get('wareAttribute')
                praise = info.get('praiseCnt')
                reply = info.get('replyCnt')
                pictures = info.get('pictureInfoList')
                result = {
                    'id': id,
                    'content': content,
                    'date': date,
                    'score': score,
                    'userNickName': user_nickname,
                    'productAttributes': product_attrs,
                    'praise': praise,
                    'reply': reply,
                    'pitcures': pictures
                }
                print(result)
                comments_collection.update_one({
                    'id': id,
                    'content': content,
                    'date': date,
                    'score': score,
                    'userNickName': user_nickname,
                    'productAttributes': product_attrs
                }, {'$set': result}, upsert=True)




