# 比较操作数的大小，并返回布尔类型的结果(Treu/False)
1 < 2
2.0 >= 1
2.0 == 2.0
2.0 != 2.0

# 混合类型运算会出现类型自动升级(自动类型转换)

# python支持连续的比较
# A < B < C ==> A < B and B < C
x = 2
y = 4
z = 6


x < y < z
x < y and y < z
x < y > z
x < y and y > z

1 < 2 < 3.0 < 4
1 > 2 > 3.0 > 4

1 == 2 < 3
