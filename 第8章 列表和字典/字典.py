D = {'spam': 2, 'ham': 1, 'eggs': 3}
D['spam']
D
len(D)

'ham' in D
# Python3取消has_key()方法
D.has_key('ham')
# keys()方法，返回dict_keys对象，它收集字典中所有的键，是一个迭代器而不是一个物理列表
D.keys()
list(D.keys())

# 原处修改
D['ham'] = ['grill', 'bake', 'fry']
D
del D['eggs']
D
D['brunch'] = 'Bacon'
D
# 迭代器
va = D.values()
list(va)
it = D.items()
list(it)
# 读取不存在的键会报错，可以使用get()，不存在时返回None对象或者设置默认值
D['a']
D.get('a')
D.get('a', 'Missing')
D.get('spam')

# update()合并，盲目覆盖相同的键
D1 = {'eggs': 3, 'ham': 1, 'spam': 2}
D2 = {'toast': 4, 'muffin': 5}
D3 = {'eggs': '覆盖'}
D1.update(D2)
D1
D1.update(D3)
D1

# pop()删除给定的键，并返回该键的值
D1.pop('eggs')
D1

table = {
    'python': 'Guido van Rossum',
    'Perl': 'Larry Wall',
    'Tcl': 'John Ousterhout',
}
language = 'python'
creator = table[language]
creator
for creator in table:
    print(creator, '\t', table[creator])

for creator in table.keys():
    print(creator, '\t', table[creator])

# 任何不可变对象都可以做键
D = {}
D[99] = 'spam'
D

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
Matrix

x, y, z = 2, 3, 4
Matrix[(x, y, z)]

# 读取稀疏矩阵
if (2,3,4) in Matrix:
    print(Matrix[(2,3,4)])
else:
    print(0)

try:
    print(Matrix[(2,6,4)])
except KeyError:
    print(0)

Matrix.get((2,5,6), 0)

# 使用字典作为记录
# 字典可以扮演多种角色：
    # 搜索数据结构
    # 表示多种结构化信息: 多种描述某一项属性的方法之一

rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'
print(rec['name'])

mel = {
    'name': 'Mark',
    'jobs': ['trainer', 'writer'],
    'web': 'www.rmi.net',
    'home': {'state': 'CO', 'zip': 80513}
}
mel['name']
mel['jobs']
mel['jobs'][1]
mel['home']
mel['home']['zip']

# # =================================字典生成/创建字典的方法
{'name': 'mel', 'age': 45}

D = {}
D['name'] = 'mel'
D['age'] = 45

# 关键字形式，键必须是字符串
dict(name = 'mel', age = 45)
# 使用键和值的序列　生成字典
dict([('name', 'mel'), ('age', 45)])
# 字典的所有值都相同，初始化字典默认为None对象
dict.fromkeys(['a', 'b'])
dict.fromkeys(['a', 'b'], 'value')

# ================================字典解析表达式
a = zip(['a', 'b', 'c'], [1, 2, 3])
list(a)
a = zip(['a', 'b', 'c'], [1, 2, 3])
D = dict(a)

D = {k : v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
D = {x : x ** 2 for x in [1, 2, 3, 4]}
D = {c : c * 4 for c in 'SPAM'}
D = {c.lower() : c + '!' for c in ['SPAM', 'EGGS', 'HAM']}

# 使用字典解析从键列表初始化字典
D = dict.fromkeys(['a', 'b', 'c'], 0)
D = {x: 0 for x in ['a', 'b', 'c']}

# ========================字典视图
# keys()\values()\items()都是返回的字典视图对象，在2.x中返回实际结果的列表
# 视图对象是可迭代的，每次产生一个结果项，而不是结果的列表
a = D.keys()
b = D.values()
c = D.items()

list(a)
for k in D.keys():
    print(k, end=' ')
# python3中字典拥有自己的迭代器，　返回连续的键，不用调用keys()
for k in D:
    print(k, end=' ')

# Python3中的字典视图是可以动态的反映出字典的变化的
D = {'a': 1, 'b': 2}
D
a = D.keys()
b = D.values()
c = D.items()
a
b
c
del D['a']
D
a
b
c

# ========================排序字典键
# 1.0
D = {'a': 1, 'b': 2, 'c': 3}
D
ks = list(D.keys())
ks.sort()
for k in ks:
    print(k, D[k])
# 2.0
ks = D.keys()
for k in sorted(ks):
    print(k, D[k])
# 3.0
for k in sorted(D):
    print(k, D[k])

# =========================字典比较大小
# python2.x字典可以使用　比较运算符　直接进行比较
# python3.x中字典可以比较排序后的

# =========================成员检测
# python2.x字典成员检测可以使用has_key()和in(成员检测运算符)
# python3.x只能使用in(成员检测运算符)或者使用带有默认测试的get()方法
