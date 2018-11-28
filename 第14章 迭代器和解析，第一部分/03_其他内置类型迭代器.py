# 内置迭代器: 文件迭代器、序列迭代器(列表、元祖、字符串)、字典迭代器

# 字典迭代器

# 1.遍历字典键，获取字典键的列表
D = {'a': 1, 'b': 2, 'c': 3}
for key in D.keys():
    print(key, '==>', D[key])

d = D.keys()        # d is dict_keys(['a', 'b', 'c'])
iter_d = iter(d)    # iter_d is <dict_keyiterator object at 0x7f5ae2d55a48>
iter_d.__next__()

# 2.自动获取字典键列表的迭代器，不在需要调用keys()方法
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '==>', D[key])
D
iter_D = iter(D)    # <dict_keyiterator object at 0x7f5ae2d55c78>
iter_D.__next__()

# shelves
# os.popen()

# range()
R = range(5)
R
iter_R = iter(R)
iter_R
# 可迭代对象一次返回一个结果，并将该结果从迭代器中删除
iter_R.__next__()
next(iter_R)
list(iter_R)

# enumerate，本身就是一个迭代器
E = enumerate('spam')
E
E.__next__()
next(E)
list(E)
# 可迭代的对象，我们把他们放到list()能够看到它们的值
