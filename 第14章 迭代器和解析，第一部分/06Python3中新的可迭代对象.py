# python3中返回的可迭代对象，不是实际的列表；需要一个个读值或者调用list()使其一次产生所有的结果

# 可迭代对象
#   文件迭代器
#   字典、keys()、values()、items()
#   序列(字符串、列表、元组)

#　 Python3中一下函数返回值为可迭代对象，而不是结果列表(节约内存空间)
#   range()
R = range(10)
R
R.__next__()    # range()返回的可迭代对象，不是一个迭代器，
list(R)
iter_R = iter(R)
iter_R.__next__()
next(iter_R)
list(iter_R)

#   一下函数与range()不同点在于，它们本身就是迭代器
#   map()
M = map(abs, (-2, -1, 0, 1, 2))
M
M.__next__()
next(M)
# iter_M = iter(M)  map返回的迭代对象自身就是一个迭代器，这个步骤非必须
list(M)
#   zip()
Z = zip((1, 2, 3), (4, 5, 6))
Z
Z.__next__()
list(Z)
#   filter()

# =====================多个迭代器 VS 单个迭代器

# =====对于range()对象
# range对象，本身不是迭代器，使用iter()函数生成迭代器
# 当有多个迭代器时互不影响，各自记住各自的位置
r = range(3)
r
# r.__next__()  'range' object has no attribute '__next__'
iter_r1 = iter(r)
iter_r2 = iter(r)
iter_r1.__next__()
iter_r2.__next__()

# =====对于zip()、map()、filter(对象)
# 这些对象本身就是迭代器，不支持多个活跃的迭代器
m = map(abs, (-1, -2, -3))
m
m.__next__()

iter_m1 = iter(m)
iter_m2 = iter(m)
iter_m1.__next__()
iter_m2.__next__()

# =====================字典视图迭代器
# 字典的keys()、values()、items()返回的是字典的视图对象
# 这些字典视图对象可以实时反应字典的变化，并且保持和字典中项相同的物理顺序

D = dict(a = 1, b = 2, c = 3)
D
# D.__next__()      'dict' object has no attribute '__next__'
ks = D.keys()
ks
list(ks)
# ks.__next__()     'dict_keys' object has no attribute '__next__'
iter_ks = iter(ks)
iter_ks.__next__()
list(iter_ks)

vs = D.values()
vs
del D['a']
vs
list(vs)
iter_vs = iter(vs)
iter_vs.__next__()
next(iter_vs)


its = D.items()

# 字典拥有自己的迭代器，返回连续的键
D = dict(a = 1, b = 2, c = 3)
D
iter_d = iter(D)
list(iter_d)
