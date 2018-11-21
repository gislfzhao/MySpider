# -*- coding: utf-8 -*-
import requests
from SpiderPractise.GetWangyiMusic.config import get_user_agent


def crawl_music_page(url):
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '_iuqxldmzr_=32; _ntes_nnid=eb6ebb280c23dceb9e9e55531f4bd0d5,1523517586694; _ntes_nuid=eb6ebb280c'
                      '23dceb9e9e55531f4bd0d5; usertrack=ezq0pVrwLp2F37wIAzR/Ag==; _ga=GA1.2.1754469600.1525690029; nts'
                      '_mail_user=gislfzhao@163.com:-1:1; mail_psc_fingerprint=5efc5fd37378ee79d7022db0f5a0678f; WM_TID'
                      '=mGlYtz5%2F2V5BAUFEFAcoLDzferJ50NTL; __f_=1540035328915; hb_MA-BFF5-63705950A31C_source=www.baid'
                      'u.com; hb_MA-BFF5-63705950A31C_u=%7B%22utm_source%22%3A%20%22weibo%22%2C%22utm_medium%22%3A%20%'
                      '22webShare%22%2C%22utm_campaign%22%3A%20%22share%22%2C%22utm_content%22%3A%20%22courseIntro%22%2'
                      'C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; Province=010; City=010; vjuid'
                      's=b7a7dbcfc.167169f867a.0.06c1ee4d898a5; vjlast=1542272813.1542272813.30; __gads=ID=a8847400779'
                      '0bb8a:T=1542273082:S=ALNI_MZ1l1WZ2AU4NxrkrN0kAoJtZz-sAQ; vinfo_n_f_l_n3=970981fed4de8639.1.1.154'
                      '2272595424.1542273204769.1542275033537; NNSSPID=e4cdb613e0674720b4ea9d48117de9b1; NTES_hp_textli'
                      'nk1=old; __utmc=94650624; playerid=73584920; JSESSIONID-WYYY=ZIWkmvNViK%2F%2B61hBJdozQyA56chByjM'
                      'xSI1wa%5CK4gnv0QT9q76vZSV%2Fsi%2B4JfRt2aZHK4C3%2FA3tp2GdYVtaxfssR3ZIAG4jcf1%5CqFOIlGq%2BqQ69WCCk'
                      'G5DyDoEMWdS4rNDfUJa3U465pN27sTbvr5EwyZ2lhxqIpzY4iEg2vUPnAh%5CwF%3A1542714167387; __utma=9465062'
                      '4.1909532803.1523517587.1542709717.1542712368.19; __utmz=94650624.1542712368.19.9.utmcsr=baidu|u'
                      'tmccn=(organic)|utmcmd=organic; WM_NI=z3XIUtqrv%2FeB9qQXdjFmedsGwLCxinMNkkELrASJJZqd2mHpkAPibo4I'
                      'M%2FpAJTnQPYVq4j2d%2BsRImlRQiKeX%2BVO528sxgOM1HMqEFGuwD4wRFM87xirk5rDnNsi7ZZ2dZW8%3D; WM_NIKE=9c'
                      'a17ae2e6ffcda170e2e6ee98fc45b5b98db2cd60869e8bb3d15b879a9fafbc6af3b09bdab46285ed98d7f02af0fea7c3'
                      'b92abaed98aad880b3aebad0e84afbaf9fb9e76286b3ab85f24db5948d99ec668f92a58cc848b29f9dabc952b3bcfe8e'
                      'cb7ca99fa08ae165f89783d0f34b8a8ca2b2d35396affc8bb170e9ad9eaaf068928fa7ace854e98a81d6b134b1a8a9b'
                      '0d03b8c93bfa6c54db7a98cd5f65a8693f8d8fb63b2b5fb93c7668eada7d8d952f2bc96b8bb37e2a3; __utmb=94650'
                      '624.18.10.1542712368',
            'Host': 'music.163.com',
            'Origin': 'https://music.163.com',
            'Referer': 'https://music.163.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': get_user_agent()
    }
    try:
        response = requests.get(url, headers=headers, timeout=20)
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except requests.RequestException as e:
        print("ERROR", e.args)
    finally:
        return None


def parse_music_page(response):
    pass


def main():
    url = "https://music.163.com/#/discover/toplist?id=2250011882"
    html = crawl_music_page(url)


if __name__ == '__main__':
    main()
