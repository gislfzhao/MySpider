# -*- coding: utf-8 -*-
import requests
import contextlib
from urllib import request
import urllib


def get_page(url):
    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 "
                          "Safari/537.1 "
    }
    # headers = {
    #     'Accept': '*/*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #     'Connection': 'keep-alive',
    #     'Content-Length': '420',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Cookie': '_iuqxldmzr_=32; _ntes_nnid=eb6ebb280c23dceb9e9e55531f4bd0d5,1523517586694; '
    #               '_ntes_nuid=eb6ebb280c23dceb9e9e55531f4bd0d5; usertrack=ezq0pVrwLp2F37wIAzR/Ag==; '
    #               '_ga=GA1.2.1754469600.1525690029; nts_mail_user=gislfzhao@163.com:-1:1; '
    #               'mail_psc_fingerprint=5efc5fd37378ee79d7022db0f5a0678f; WM_TID=mGlYtz5%2F2V5BAUFEFAcoLDzferJ50NTL; '
    #               '__f_=1540035328915; hb_MA-BFF5-63705950A31C_source=www.baidu.com; '
    #               'hb_MA-BFF5-63705950A31C_u=%7B%22utm_source%22%3A%20%22weibo%22%2C%22utm_medium%22%3A%20%22webShare'
    #               '%22%2C%22utm_campaign%22%3A%20%22share%22%2C%22utm_content%22%3A%20%22courseIntro%22%2C%22utm_term'
    #               '%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; Province=010; City=010; '
    #               'vjuids=b7a7dbcfc.167169f867a.0.06c1ee4d898a5; vjlast=1542272813.1542272813.30; '
    #               '__gads=ID=a88474007790bb8a:T=1542273082:S=ALNI_MZ1l1WZ2AU4NxrkrN0kAoJtZz-sAQ; '
    #               'vinfo_n_f_l_n3=970981fed4de8639.1.1.1542272595424.1542273204769.1542275033537; '
    #               'WM_NI=6uo5sBEtAeKkXbRRYE4nbJKJeYhPOWvkOdrLtC70tTofR8L8pzeZ4Q66yBVDrXZkLTq%2BHoK8e'
    #               '%2FQuJPaZqeHkejcr1hZRHaFShrGU72yz5hXsImbqESOozHemRX6LjxSVY1o%3D; '
    #               'WM_NIKE'
    #               '=9ca17ae2e6ffcda170e2e6ee83d139b595f89bce528fbc8ab3c85e939e8eaab76bb5a7a987ae39fbf0bab2c12af'
    #               '0fea7c3b92af6aba1d6f24a87ac8f86ca619cbe9eb3dc4ff8b2aeabca42a787a8b1ce5db6b58185f148b89df9d1f760ad'
    #               'ba9ed9cf34b4a6abbbb75bf6eab7a3d550b288968ccf60b3f58890ca34a7f19f96c95ca386bf86cb61a7b6ad93b4649a8'
    #               'e8882c559acae89b6b63abba6fb89db798bb3ae92c8598db1b6a9e8679288faade974918a97d2ee37e2a3; NNSSPID=e4c'
    #               'db613e0674720b4ea9d48117de9b1; NTES_hp_textlink1=old; JSESSIONID-WYYY=SHHjZ%5CjFb2H8tirV9tEx7BmQdC'
    #               'EZAaeKG7wWcE34rtnZic4mCsM5pNr5DzBoAH8Yuxta%2FtFH5MqJqsiDl25r6W8o6MOn56dETR8amzISDJr7kd5zxb7459b%5'
    #               'CZIvWV84tFsxYY3VRwTfE1%5CXywUDfDswD6b4ayaQwG3TWw%2FhXcWUzOXcg%3A1542698986982; __utma=94650624.19'
    #               '09532803.1523517587.1542674953.1542697187.17; __utmc=94650624; __utmz=94650624.1542697187.17.8.ut'
    #               'mcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=94650624.5.10.1542697187',
    #     'Host': 'music.163.com',
    #     'Origin': 'https://music.163.com',
    #     'Referer': 'https://music.163.com/',
    #     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 "
    #                   "Safari/537.1 "
    # }
    # data = {
    #     'params': 'sOfSZUU8l%2FVFhcybeB%2Fz%2BzwA8eky7EU%2BjPsoQ1Zho6oA%2BA4EhTBU%2Bej3%2BhpcMhE1S8kbRqaEU%2Bv9Xyo56ZhZ'
    #               'dIq%2BMhZKZlS41WLHcs9aorySy8ABH5raQ6PSRFKOekbi',
    #     'encSecKey': 'd6e5c1e3b8fde86223187df3fb68164eb4705635b9dceea852220358abcd7cc89216b81d54d7ee1113d191e9698edb41'
    #                  'fc0316274f4e5aa2341ed53860f2aa4f433222b60ab062c4ed3f833433cf8da9b28251feb2170bf358920ebd53d40950d'
    #                  'ad3fa40bc1968a225105f3618db819ee8c3bb4ecbce67bce41aaa8498b2185b'
    # }
    try:
        counter = 0
        with contextlib.closing(requests.get(url=url, headers=headers, stream=True)) as fp:
            with open('result2.mp3', 'wb') as f:
                for chunk in fp.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        counter += 1
                        if counter == 100:
                            f.flush()
                            counter = 0
        # save_mp3(response)
        # print(response.status_code)
        # print(len(response.content))
        # if response.status_code == 200:
        #     print(200)
        #     return response
    except requests.RequestException as e:
        print("ERROR", e.args)


def parse_page(response):
    print(response)
    if response:
        save_mp3(response)


def save_mp3(response):
    with open("result1_music.mp3", 'wb') as f:
        f.write(response.content)


def save_file():
    pass


def main():
    mp3_url = "http://m10.music.126.net/20181120152536/eff313c2ffaa645faedc2571a47231b2/ymusic/341e/9cc2/7c4f" \
              "/b13ac6e62d3625524dde95fd1b1628bf.mp3 "

    # request.urlretrieve(mp3_url, filename='re.mp3')
    # get_page(mp3_url)
    url = 'http://m10.music.126.net/20181120190053/ccc352cff525bdfa90a2be2e1e2ba8b3/ymusic/04cb/a0b0/da37/611c5bfd91ee07158116fed0b0521609.mp3'
    with contextlib.closing(requests.get(url=url, stream=True)) as fp:
        with open('无处安放.mp3', 'wb') as f:
            for chunk in fp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
    # requests.urlretrieve(url=mp3_url, filename="rrr.mp3")

    # requests.urlretrieve(url=url, filename='1.jpg')


def get_test():
    print("test")
    for i in range(5):
        con = i
        print(con)
        yield con
        
    # for i in range(10, 15):
    #     print(i)


def a():
    for i in range(3):
        print(i)
        yield i

    for i in range(6, 9):
        print(i)
        yield i


if __name__ == '__main__':
    for i in a():
        pass
    # a = get_test()
    # print(next(a))
    # print(next(a))
    # main()
