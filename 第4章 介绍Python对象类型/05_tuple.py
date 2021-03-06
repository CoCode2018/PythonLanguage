# 元组
# 序列的一种，拥有从左到右的顺序通过位置存取；可以嵌套任意类型的对象；不可变对象类型(可以看做不可变的列表)

T = (1, 2, 3, 4)
len(T)

# ==========序列操作
# 索引
T[0]
# 切片
T[0:3]
# 拼接，不可变对象类型，返回新的元组
T + (5, 6)
# 重复
T * 2
# 支持任意类型对象的嵌套
T = ('spam', 3.0, [11, 22, 33])
T[1]
T[2][2]

# 元组自己是不可变的对象，不能改变大小，但是如果嵌套的对象是可变对象类型可以改变嵌套的对象
T[2].append(44)
T

# ==========特定的操作
# Python3之前元组没有任何方法，Python3为元组添加了两种方法
# index()，返回给定值第一次出现的位置索引
T.index(3)
# count()，返回给定值在元组中出现的次数
T.count(2)

# ==========为什么还要提供元组
# 元组提供一种完整性的约束，编写大型程序更方便
