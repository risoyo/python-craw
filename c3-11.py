# coding=utf-8
import requests
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def qiubai():
    file_abs = "D:\\Nowcoder-Java\\python-craw"
    content = requests.get('https://www.qiushibaike.com/').content
    soup = BeautifulSoup(content, 'html.parser')
    file_content = file_abs + "\\content" + ".txt"
    f = open(file_content, "wb")
    for div in soup.find_all('div', {'class': 'content'}):
        f.write(div.text.strip().encode('gbk'))
        f.write('\r\n')
    f.close()


if __name__ == '__main__':
    qiubai()
