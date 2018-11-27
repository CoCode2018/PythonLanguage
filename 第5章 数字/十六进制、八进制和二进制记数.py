# 八进制
0o1, 0o2, 0o377, 0O1, 0O2, 0O377
# 十六进制
0x01, 0x10, 0xFF, 0X01, 0X10, 0XFF
# 二进制
0b1, 0b10000, 0b11111111, 0B1, 0B10000, 0B1111111

# 它们都是十进制整数对象的一种表现形式，内存中指向的是同一个整数对象

# 十进制转换函数，返回结果是一个字符串
oct(64)
hex(64)
bin(64)
# int()接受一个数字字符串和这个数字字符串的基数，默认是10
int('64')
int('100', 8)
int('40', 16)
int('1000000', 2)
# eval()函数接受一个字符串参数，会把这个字符串作为代码执行
eval('64')
eval('0o100')
eval('0x40')
eval('0b1000000')

# 格式化显示整数
'%o, %x, %X' % (64, 255, 255)
'{0: o}, {1: x}, {2: b}'.format(64, 64, 64)