# coding=utf-8
import random
import re


def things_print(num, con):
    print num,
    print con


def demo_string():
    sa = 'hello world'
    things_print(1, sa.capitalize())  # 转为大写
    things_print(2, sa.replace('world', 'you'))  # 替换
    sb = '   \r\n hello \r\n'
    things_print(3, sb.strip())  # strip()方法删除指定元素，默认删除空格，也可以加入‘0’来删除0：strip（‘0’）
    things_print(4, '-'.join(['a', 'b', 'c']))  # 用-把join中全部的元素连起来，相当于连续的+=
    things_print(5, sb.find('ello'))  # 用-把join中全部的元素连起来，相当于连续的+=


def demo_operation():
    a = 5
    b = 5.0
    print a, type(a)
    print b, type(b)
    pass


def demo_build_function():
    print 1, max(1, 5), min(1, 5)
    print 2, len('xxx')
    print 3, abs(-1)
    print 4, dir(list)  # 列出当前对象有哪些方法
    x = 3
    print 5, eval('x+3')  # 直接执行一段代码
    print 6, chr(65), ord('a')  # 数字转ascii与ascii转数字
    pass


def demo_exception():
    try:
        print 2 / 0
    except Exception as e:  # 若遇到异常，就将异常打印出来，保存到e中
        print 'error', e
    finally:
        print 'clear'
    pass


def demo_random():
    random.seed(1)  # 随机数的生成依赖于seed，是以seed为基数运算后所得，所以都是伪随机
    r = random.randint(0, 100)  # 生成0-100的随机数
    print 2, random.choice(range(1, 100))
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)  # 打乱a的顺序
    print a
    pass


def demo_regex():
    sa = 'abc123def12gh15'
    p1 = re.compile('[\d]+')  # 匹配所有连续数字组 exp['123', '12', '15']
    p2 = re.compile('\d')  # 匹配所有单个数字 exp['1', '2', '3', '1', '2', '1', '5']
    p3 = re.compile('[^\d]+')  # 匹配所有非数字
    print 1, p1.findall(sa)
    print 2, p2.findall(sa)
    print 3, p3.findall(sa)
    sb = 'abc@163.com,bdf@163.com,fjld@qq.com,ejqowi@gmail.com,adlsj@hotmail.com,a@qq.com'
    p4 = re.compile('[\w]+@[163|qq]+\.com')  # [\w]+表示匹配单个或多个字母数字，@表明必须以@连接，[163|qq]+表示两个至少有一个，再接上转义的
    print 4, p4.findall(sb)  # .(\.)，最后必须以com结尾
    sc = '<html><h>title</h><body>content</body></html>'
    p5 = re.compile('<h>[\w]+</h>')  # 匹配<h></h>之间的标题，body同理
    p5_str = str(p5.findall(sc))
    print 5, 'title: ', p5_str[p5_str.index('<h>') + 3:p5_str.index('</h>')]  # 将匹配结果转为字符串之后截取字符串，只输出title内容
    sd = 'xx2016-08-20zzz,20139-22-11'
    p6 = re.compile('[\d]{4}-[\d]{2}-[\d]{2}')  # 匹配年月日[\d]表示任意数字{4}表示数字必须为4位
    print 6, p6.findall(sd)  # 正则表达式用来匹配，具体的判断应交给程序来做
    date_collect = []
    date_verify = []
    date_collect = p6.findall(sd)  # 注意！！！！！findall()直接返回了list存储的所有匹配到的字符串
    for i in date_collect:  # \d 数字 \D 非数字 ＼s 空格 \S 非空格 \w 单词字符 \W 非单词字符
        c = i.split('-')  # + 匹配一次或若干次 * 匹配0次或若干次 ？ 匹配0次或1次
        if 0 <= int(c[1]) <= 12 and 0 <= int(c[2]) <= 30:  # | a或b ^ 以这个开头 （）分组 \ 转义
            date_verify.append(c)

    pass


if __name__ == '__main__':
    # demo_string()
    # demo_operation()
    # demo_build_function()
    # demo_obj()
    # demo_exception()
    # demo_random()
    demo_regex()
