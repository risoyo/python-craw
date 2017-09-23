# coding=utf-8
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


if __name__ == '__main__':
    # demo_string()
    # demo_operation()
    demo_build_function()
