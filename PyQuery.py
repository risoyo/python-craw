# coding=utf-8
from pyquery import PyQuery

if __name__=='__main__':
    q = PyQuery(open('temp.html').read())  ## 读出文件内容放入pyquery中
    title = q('title').text()  # 寻找q中标签为title的元素
    print title
    # for each in q('div.menu-txt-box>ul>li>a').items():  # div.后面不能有空格，不知道咋整,只能说class带空格的要用其他方式索引了
    #     print each.attr.href
    # for each in q('#menubox>ul>li>a').items():  # '#'是根据id选择，要根据具体的格式来层层筛选，>表示下一层级的筛选方式
    #     print each.attr.href

    for each in q('div.name_left>a>b').items():
        print each.text()
