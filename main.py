# encoding:utf-8
import random
import time

import requests
from bs4 import BeautifulSoup


def get_webdata(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    r = requests.get(url, headers=headers)
    c = r.content
    b = BeautifulSoup(c, "html.parser")
    data_list = b.find('ul', {'class': 'article-ul'})
    data_li = data_list.findAll('li')
    f = open("WeChat_title.txt", "a")
    for i in data_li:
        title = i.find('h4').find('a').get_text().replace('"', '\'\'')
        link = i.find('h4').find('a').attrs['href']
        print title
        a = '<a href="' + link + '">' + title + '</a>'
        f.write(a.encode('utf8') + '\n')
    f.close()


def get_urls_webdatas():
    with open('config.txt') as config:
        config_list = config.readlines()
    config.close()
    for i in config_list:
        url = 'http://www.gsdata.cn/query/article?q=' + i.replace("\n",
                                                                  "") + '&search_field=4&post_time=3&sort=-3&cp=0&range_title=1&range_content=1&range_wx=0'
        print url
        get_webdata(url)
        time.sleep(round(random.random(), 1))


if __name__ == '__main__':
    get_urls_webdatas()
