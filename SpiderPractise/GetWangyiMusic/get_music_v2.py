# -*- coding: utf-8 -*-
import json
import os
import requests
from time import sleep
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from SpiderPractise.GetWangyiMusic.config import get_user_agent

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'music.163.com',
            # 'Origin': 'https://music.163.com', # 适用于POST请求
            'Referer': 'https://music.163.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': get_user_agent()
}


def get_music_lists():
    """
    获取网易云音乐榜单  不能出现多个yield
    :return:
    """
    html = browser.page_source
    # 其实问题就出在xmlns="http://www.w3.org/1999/xhtml"这里，pyquery默认解析后的文档是xmlns格式
    doc = pq(html, parser='html')
    toplist = doc('#toplist')
    toplistname1 = toplist('#toplist > div.g-sd3.g-sd3-1 > div > h2:nth-child(1)').text()
    toplistname2 = toplist('.n-minelst > h2:nth-child(3)').text()
    lists1 = toplist('.n-minelst > ul:nth-child(2) li.mine').items()
    for item in lists1:
        result = {
            'toplist': toplistname1,
            'id': item.attr('data-res-id'),
            'name': item('.name > a').text(),
            'link': 'https://music.163.com' + item('.name > a').attr('href'),
            'update': item('p.s-fc4').text()
        }
        print(result)
        yield result

    lists2 = toplist('.n-minelst > ul:nth-child(4) li.mine').items()
    for item in lists2:
        result = {
            'toplist': toplistname2,
            'id': item.attr('data-res-id'),
            'name': item('.name > a').text(),
            'link': 'https://music.163.com' + item('.name > a').attr('href'),
            'update': item('p.s-fc4').text()
        }
        print(result)
        yield result


def get_musics():
    """
    获取歌曲信息列表
    :param html:
    :return:
    """
    html = browser.page_source
    doc = pq(html, parser='html')
    song_list_div = doc('#song-list-pre-cache')
    toplist = doc('#toplist > div.g-mn3 > div > div.g-wrap > div > div.cnt > div > div.hd.f-cb > h2').text()
    songs = song_list_div('.m-table > tbody > tr').items()
    for song in songs:
        result = {
            'toplist': toplist,
            'id': song.attr('id'),
            'songname': song('td:nth-child(2) .ttc b').attr('title'),
            'song_link': song('td:nth-child(2) .ttc a').attr('href'),
            'duration': song('span.u-dur').text(),
            'artist': song('td:nth-child(4) span').attr('title'),
            'artist-link': song('td:nth-child(4) a').attr('href')
        }
        # print(result)
        yield result


def write_lyric(list_name, song_name, lyric):
    file_path = '{0}/{1}_lyric.{2}'.format(list_name, song_name, 'txt')
    if os.path.exists(file_path):
        print('歌曲{}的歌词已经存在'.format(song_name))
    else:
        try:
            if lyric:
                print("正在下载歌曲{}的歌词".format(song_name))
                with open(file_path, 'a', encoding='utf-8') as fp:
                    fp.write(lyric)
                print('歌曲{}的歌词下载成功！'.format(song_name))
            else:
                print("无法获取歌曲{}的歌词".format(song_name))
        except Exception as e:
            print('歌曲{}的歌词下载出错'.format(song_name), e.args)


def get_song_lyric(song_id):
    headers['Host'] = 'music.163.com'
    song_lyric_url = "http://music.163.com/api/song/lyric?id={}&lv=1&kv=1&tv=-1".format(song_id)
    try:
        res_lyric = requests.get(song_lyric_url, headers=headers, timeout=20)
        if res_lyric.status_code == 200:
            lyric = res_lyric.json().get('lrc').get('lyric')
            return lyric
    except TimeoutException:
        get_song_lyric(song_id)
    except Exception as e:
        print(song_id, "ERROR", e.args)
    return None


def download_song(list_name, song_name, song_id):
    singer_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id)
    print('正在下载歌曲：{}'.format(song_name))
    file_path = '{0}/{1}.{2}'.format(list_name, song_name, 'mp3')
    if os.path.exists(file_path):
        print('歌曲{}已经存在'.format(song_name))
    else:
        try:
            headers['Host'] = 'music.163.com'
            # 首先关闭重定向，判断singer_url是否能重定向，重定向会影响headers中的Host
            # 由于singer_url包含music.163.com域名，且初始的headers中的Host(请求资源的主机号)为music.163.com
            # 两者保持一致性， 可以保证能被正确访问
            res = requests.get(singer_url, headers=headers, stream=True, allow_redirects=False)
            print(res.headers)
            print(res.status_code, res.is_redirect)
            if res.headers.get('Location'):     # 如果headers中含有'Location', 则表明存在重定向, 即res.is_redirect=True
                print(res.headers.get('Location'))
                if '//music.163.com/404' in res.headers.get('Location'):    # 重定向资源不存在
                    print('歌曲{}的下载资源无效！'.format(song_name))
                else:
                    headers['Host'] = 'm10.music.126.net'
                    headers['User-Agent'] = get_user_agent()
                    requests.urlretrieve(res.headers.get('Location'), file_path, headers=headers)
                    print('歌曲{}下载成功！'.format(song_name))
            else:   # 无重定向，即res.is_redirect=False
                headers['Host'] = 'music.163.com'
                headers['User-Agent'] = get_user_agent()
                requests.urlretrieve(singer_url, file_path, headers=headers)
                print('歌曲{}下载成功！'.format(song_name))
        except Exception as e:
            print('歌曲{}下载过程中出错'.format(song_name), e.args)


def save_songs_from_lists(list_songs):
    # print(len(list(list_songs)))
    for song in list_songs:
        list_name = song.get('toplist', '音乐榜')
        # 判断存储榜单文件夹是否存在
        if not os.path.exists(list_name):
            os.mkdir(list_name)
        song_id = song.get('song_link').replace('/song?id=', '')
        song_name = song.get('songname')
        download_song(list_name, song_name, song_id)
        song_lyric = get_song_lyric(song_id)
        write_lyric(list_name, song_name, song_lyric)
        sleep(1)


def music_index_page():
    """
    网易云音乐首页
    :return:
    """
    try:
        url = "https://music.163.com/"
        browser.get(url)
        sleep(1)
        # 判断网易云首页导航栏加载完毕
        top_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '#g_nav2 > div > ul > li:nth-child(2) > a')))
        top_list.click()
        wait.until(EC.presence_of_element_located((By.ID, 'g_iframe')))
        browser.switch_to.frame('g_iframe')
        sleep(3)
    except TimeoutException:
        music_index_page()
    except Exception as e:
        print("ERROR", e.args)


def main():
    # music_index_page()
    browser.get('https://music.163.com/#/discover/toplist?id=2250011882')
    sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, 'g_iframe')))
    browser.switch_to.frame('g_iframe')
    sleep(2)
    list_songs1 = get_musics()
    # for song in list_songs1:
    #     print(song)
    save_songs_from_lists(list_songs1)
    sleep(2)


if __name__ == '__main__':
    # main()
    # get_song_lyric('1323302330')
    # download_song('kong', '1323303004')
    browser.quit()
    del headers['Host']
    res = requests.get('http://music.163.com/song/media/outer/url?id=554191055.mp3', headers=headers, stream=True,
                       allow_redirects=True)
    print(res.url)
    print(res.reason)
    print(res.is_redirect)
    print(res.status_code)
    print(res.headers)
    res = requests.get('http://m10.music.126.net/20181121205900/c3f4b93985aad91e28cc17486415c028/ymusic/66c8/0941/1349/c3a847fae64a90b36a8a8169a2dc2d5f.mp3',
                       headers=headers, stream=True, allow_redirects=True)
    print(res.url)
    print(res.status_code)
    print(res.is_redirect)
    print(res.reason)
    print(res.headers)
    # requests.urlretrieve('http://m10.music.126.net/20181121172426/9ff44e6a07409fd9dbd095fd91ee0a94/ymusic/66c8/0941/1349/c3a847fae64a90b36a8a8169a2dc2d5f.mp3',filename='test.mp3', headers=headers)
    # res = requests.get('http://music.163.com/song/media/outer/url?id=1323303004.mp3', headers=headers, stream=True, allow_redirects=False)
    # requests.urlretrieve('http://m10.music.126.net/20181121172747/999e8704204848cafc28340d3308e3a9/ymusic/4614/ef38/ccfb/26965dc060c6d3f9bc5c6bae01c70516.mp3', filename='test2.mp3', headers=headers)
    # print(res.headers)
    # res = requests.get('http://music.163.com/song/media/outer/url?id=1323302330.mp3', headers=headers, stream=True, allow_redirects=False)
    # print(res.headers)
    # headers['Host'] = 'm10.music.126.net'
    # requests.urlretrieve('https://m10.music.126.net/20181121185528/8df62abd3c6948488b01c56ed91446ea/ymusic/9a65/8802/9928/08ddf3d2f54a4686f22266dfa6cbde62.mp3', headers=headers, filename='test3.mp3')


