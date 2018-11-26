# 字典(dictionary)
# 字典是一种映射(mapping)，通过键值对而不是位置进行存取，没有任何可靠的顺序
# 可以包含任意的对象类型(键必须是字符串-值是可以是任意类型)，是可变的对象类型

# 映射操作
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# 通过键对值进行访问，键必须是字符串
D['food']
# 可变的对象类型
D['quantity'] += 1
D

# 与列表超边界赋值不同字典，字典可以通过新键来赋新值
D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
D
D['name']

# 重坊嵌套
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 40.5}
rec['name']
rec['name']['last']
rec['job']
rec['job'][-1]
rec['job'].append('janitor')
rec['job']
rec

# ==========键的排序： for循环
# 字典是通过键值对进行索引的，没有左右顺序，如果在一个字典上强调顺序该怎么做？
# 通过keys()方法收集键的列表，使用sort()对键列表排序，然后使用for循环显示
D = {'a': 1, 'b': 2, 'c': 3}
type(D.keys())
Ks = list(D.keys())
Ks.sort()
for key in Ks:
    print(key,"==>",D[key])

# 使用sorted()内置函数，直接返回排序的列表(默认升序，对于字典返回的是键排序的列表)
D = ['a': 1, 'c': 3, 'b': 2]
sorted(D)
for key in sorted(D):
    print(key,"==>",D[key])

a = [1,3,4,2]
sorted(a)
b = (1,3,4,2)
sorted(b)

# ==========迭代和优化===不懂？？？
# for循环和列表解析表达式是通用的迭代工具可以用于任何遵守迭代协议的任意对象
# 迭代协议：内存中物理存储的序列或者每次迭代都能产生一个元素的对象
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
squares

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)

# 尽管for循环可以实现列表解析相同的功能但是
# 列表解析和相关的函数编程工具(map、filter)通常运行的比for循环快
# Python中一个主要的原则是：首先为了简单和可读性去编码，在程序可以工作，并证明确实有必要考虑性能之后再考虑优化的问题

# ==========不存在的键：if测试
# in表达式允许我们查询字典中一个键是否存在，并可以通过if语句对结果进行分支处理
D = {'a': 1, 'b': 2}
'f' in D
'f' not in D
# //what's mean?
not 'f' in D

if 'f' not in D:
    print("missing")

# 还有其他的方法来避免获取不存在的字典键
# get()方法，该有一个默认值的条件索引
D.get('f', 0)
# if/else表达式
D['x'] if 'x' in D else 0
# try语句
