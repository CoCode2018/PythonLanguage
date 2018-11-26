# 字符串对象类型

# 1.字符的集合，Python序列对象中的一种(字符串、列表、元组)
# 2.序列是包含其他对象的有序集合
# 3.序列中的元素包含一个从左到右的顺序，可以根据它们的对应位置进行存取和操作
# 4.Python中没有字符类型，字符看做单个字符的字符串序列

# ====================序列的操作(索引、切片、拼接、重复)

# Python变量不用进行声明，变量在第一次赋值时创建出来，并且可以赋予、替换任意类型的值
S = 'Spam'
# 变量在使用之前必须要创建出来也就是必须要进行第一次赋值
len(S)
# ===========Python中索引从0开始
S[0]
S[1]
# ===========Python中可以反向索引，倒数第一个元素的索引是-1
S[-1]
# -1 和 len(s) + (-1)索引的值是同一个
S[len(S) - 1]   
S[-2]

# ===========切片(slice): 从序列中提取元素的方法
# X[I:J]: 从X序列中取出从偏移量为I的元素开始，直到偏移量为J的元素但不包含J元素(从I到J-1）的内容
S[1:3]
# 切片操作的左边界默认为0
# 右边界默认为整个序列的长度
S[0:3]
S[:3]
S[1:4]
S[1:]
S[:-1]
S[:]    # 对一个序列进行拷贝

# ===========拼接
S + 'xyz'
# ===========重复
S * 8
# 对于序列的重复和拼接，利用了Python多态的特性：
# 多态：一个操作的实际意义取决于被操作的对象，
#      只要被操作的对象支持这种兼容的接口，那这个被操作的对象就能够进行这种操作，并且结果由对象兼容的接口定义的行为决定

# ====================Python中每个对象都分为不可变性和可变性
#   不可变：数字、字符串、元组
#   可变： 列表、字典
# 字符串是不可变对象类型
# 'str' object does not support item assignment
# S[0] = 'z'
# 可以通过对同一个变量赋予一个新的字符串对象
S = 'z' + S[1:]

# ====================类型特定的方法
# 一旦对象创建出来，除了绑定一些通用操作之外还绑定了一个特定类型的操作集合(该对象类型的方法)
# 多种类型的通用操作都是以内置函数或者表达式形式出现
# 特定类型的操作是通过方法调用的形式出现
# 因为字符串是不可变的对象类型，因此这些方法都是返回一个新的字符串

# find()在字符串中寻找子字符串，返回子字符串的索引或者-1(没有找到)
S.find('z')
S.find('b')
S.find('zp')
S.find('za')

# replace()对字符串进行全局的搜索并替换
S.replace('z', 'S')

# split()对字符串进行解析，返回一个解析列表
line = 'aaa,bbb,ccc,ddd'
line.split(',')

# upper() 大写
S.upper()

# lower() 小写
S.lower()

# isalpha()测试是否是字符
S.isalpha()

# isdigit()测试是否是数字
S.isdigit()

# rstrip() 去掉字符串后的空格
line = 'aaa,bbb,ccc\n'
line.rstrip()

# 字符串格式化显示
'%s, eggs, and %s' % ('spam', 'SPAM!')
'{0}, eggs, and {1}'.format('spam', 'SPAM!')
a = 'spam'
b = 'SPAM!'
f"{a}, eggs, and {b}"


# ====================寻求帮助
dir(str)
help(str.replace)


# ====================编写字符串的其他方法
# 转义序列
S = 'A\nB\tC'
len(S)
# ASCII 值
ord('\n')
ord('a')
ord('A')
# Python字符串可以包括在单引号、双引号、三引号(三个单引号或者三个双引号，作用是多行原样显示)中，表示相同的含义
'Zapm'
"Zapm"
# 自动的在末尾添加换行符，print输出时自动解析
msg = """aaaa
bbb'''bbbbbb""bbbb'bbbb
cccccccccc"""
print(msg)
# 原始字符串，去掉反斜线的转义机制，以r开头


# ====================模式匹配
# 字符串支持基于模式的文本处理
import re
match = re.match('Hello[ \t]*(.*)world', 'Hello    Python world')
match.group(1)
match = re.match('Hello[\t]*(.*)world', 'Hello    Python world')
match.group(1)

match = re.match('/(.*)/(.*)/(.*)', '/usr/bin/python')
match.group()
match.group(1)
match.group(2)
match.group(3)
match.groups()
list(match.groups())