len([1, 2, 3])
[1, 2, 3] + [4, 5, 6]
['Ni'] * 4
# ＋拼接操作两边的操作数必须是相同类型
str([1, 2]) + '34'
[1, 2] + list('34')

3 in [1, 2, 3]
for x in [1, 2, 3]:
    print(x, end=' ')

res = [c * 4 for c in 'spam']
res

res = []
for x in 'spam':
    res.append(x * 4)
res
# 内置map()函数做类似列表解析的工作，它是对序列中的每一项引用一个函数，返回一个map对象，可以使用list()导出
a = map(abs, [-1, -2, 0, 1, 2])
list(a)

L = ['spam', 'Spam', 'SPAM!']
L
L[2]
L[-2]
L[1:]

matrix = [
    [1, 2, 3,],
    [4, 5, 6,],
    [7, 8, 9,],
]
matrix
matrix[1]
matrix[1][1]
matrix[2][0]

L = ['spam', 'Spam', 'SPAM!']
L
L[1] = 'eggs'
L
L[0 : 2] = ['eat', 'more']
L

# append()和sort()返回None对象，如果使用赋值则会失去原来的列表
L.append('please')
L
L.append([1,2,3])
L
L.pop()
L.sort()
L
#　extend()会自动解析参数，作为多个元素插入列表
L.extend([1,2,3])
L
L.extend("34")
L
L.extend((1,2,3))
L
# pop()默认删除最后一个元素并返回删除的元素；也可以接受一个索引值
L.pop(0)
# remove()接受一个列表元素内容参数，返回None对象
L.remove('please')
# reverse()反转列表
L.reverse()

# 接受两个参数，一个是索引为止；一个是插入的值
L.insert(0, '你')
# 返回给定值的索引，会报错
L.index('你')

del(L[0])
L

del L[1:]
L

L[:] = []
L

# 将空列表赋值给一个索引，会在该位置存储空列表的引用，而不是删除
L.append(0)
L[0] = []
L