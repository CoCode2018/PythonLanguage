# Python迭代协议相关概念

# for循环可以用于任何可迭代的对象
# 所有会从左至右扫描对象的迭代工具，都可以用于序列等可迭代对象上

# 可迭代对象(实际序列和按照需求而计算的虚拟序列)
#   1.对象实际保存的是序列
#   2.可以在迭代工具环境中，一次产生一个结果的对象

f = open('script.py', 'w')
f.write('import sys\n')
f.write('print(sys.path)\n')
f.write('x = 2\n')
f.write('print(2 ** 33)\n')
f.close()
# ================文件迭代器
# 常规读取文件，到达文件尾时返回空字符串
# 可以通过检测空字符串来判断是否到达文件尾，而跳出循环
file = open('script.py', 'r')
file.readline()
file.readline()
file.readline()
file.readline()
file.close()
# 文件对象内部有一个__next__方法，返回文件下一行，到达文件尾时会引发内置异常(StopIteration)
file = open('script.py', 'r')
file.__next__()
file.__next__()
file.__next__()
file.__next__()
file.close()

# 这个__next__接口就是python中的迭代协议: 
#   有__next__方法的对象会前进到下一个结果，并且在一系列结果的末尾时会引发StopIteration
# Python中任何这类对象都认为是可迭代的，迭代工具就可以用在这些对象上，内部就是调用__next__方法，并捕捉异常确定离开时机

# 因此逐行读取文本文件最好的方式根本不去读取而是使用文件迭代器
for line in open('script.py', 'r'):
    print(line, end=' ')
# 或者: 将整个文件加载到内存做成行字符串列表
# 这并不是一个好方式，当文件太大时一次性读取性能不好；内存不够时会不工作
# 迭代器行读取不会出现内存爆炸的问题
for line in open('script.py', 'r').readlines():
    print(line, end=' ')

# 也可以使用while循环读取文件，速度要慢一些，迭代器是以C语言速度运行的
# while是以Python字节码运行的
file = open('script.py', 'r')
while True:
    line = file.readline()
    if not line: break
    print(line, end=' ')

