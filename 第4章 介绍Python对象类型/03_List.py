# 列表
# 序列的一种，任意类型对象的位置相关的有序集合，是可变的对象类型(大多数操作是原位置修改)，没有固定长度

# ==========序列的操作
# 1.可包含任意类型的对象
L = [123, 'sapm', 1.23]
len(L)
# 2。索引
L[0]
# 3.切片(slice)
L[:-1]
# 4.拼接，返回新的列表不会原位置修改
L + [4, 5, 6]
# 5.重复，返回新的列表不会原位置修改
L * 5

# ==========类型特定的操作
# append()，返回None对象，进行原位置修改
L.append('NI')
# pop()，返回索引位置的对象，不改变列表
L.pop(2)
# del()，删除操作，原位置修改
del(L[2])
# insert()，在索引位置添加元素，原位置修改
L.insert(2, 1.23)
# remove()，移除列表中参数提供的元素，原位置修改
L.remove(1.23)
# sort()，对列表进行排序，默认为升序，原位置修改
M = ['bb', 'cc', 'aa']
M.sort()
# reverse()，对列表进行翻转，原位置修改
M.reverse()

# ==========边界检查
# Python不允许访问不存在的元素，访问超边界的元素会报错
L[99]
# 对于超边界的赋值，Python不会增大列表而是报错，为了让列表增大可以使用append()
L[99] = 1

# ==========嵌套
# Python列表支持任意的嵌套，类型和层次都是任意的
# 多维数组
M = [
        [1, 2, 3,],
        [4, 5, 6,],
        [7, 8, 9,],
    ]
M
M[1]
M[1][2]

# ==========列表解析(列表、字典、集合、生成器)
# 列表解析表达式(list comprehensive expression)
# 返回的结果是列表，列表解析可以用在任意的可迭代的对象类型上
for row in M:
    print(row)
[row[1] for row in M]
[row[1] + 1 for row in M]
[row[1] for row in M if row[1] % 2 == 0]

[M[i][i] for i in [0, 1, 2]]
[c * 2 for c in 'spam']

# ()中的解析表达式不能创建一个元组，而是返回一个生成器
G = (sum(row) for row in M)
next(G)

# {}中的解析表达式可以创建字典或者集合
[sum(row) for row in M]
{i: sum(M[i]) for i in range(3)}

# 列表、集合、字典都可以用列表解析
[ord(x) for x in 'spaam']
{ord(x) for x in 'spaam'}
{x: ord(x) for x in 'spaam'}