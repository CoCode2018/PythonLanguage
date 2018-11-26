# 数字对象类型

123 + 222
1.5 * 4
# Python3只有一个整型(长整型)，自动提供额外的精度保存较大的整数值
2 ** 100
# object of type 'int' has no len()
len(str(2 ** 1000000))
# 对象有两种打印方式：
#   对象的代码形式(repr())
#   对象的用户友好形式(str())
3.1415 * 2

# math模块提供更高级的数学工具
import math
math.pi
# 平方根
math.sqrt(85) 

# random模块提供随机数生成器和随机选择器
import random
# 在[0,1)之间生成一个随机数
random.random()
# 在一个序列里随机选择
random.choice([1, 2, 3, 4])
# I don't know
#random.choices()