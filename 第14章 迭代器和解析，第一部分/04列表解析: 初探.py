# 列表解析的语法源自集合理伦表示法中的一个结构，该结构对集合中的每个元素应用一个操作

# ====================列表解析
# 在遍历列表时，修改列表
L = [1, 2, 3, 4]
for i in range(len(L)):
    L[i] += 10

# 使用列表解析，运行速度更快，它会产生一个新的列表
L = [1, 2, 3, 4]
res = [x + 10 for x in L]

# 和列表解析做相同的事情，使用列表解析速度快一倍
L = [1, 2, 3, 4]
res = []
for x in L:
    res.append(x+10)

# ====================文件上使用列表解析
file = open('script.py', 'r')
# readlines()直接把文件载入内存，返回行字符串列表
lines = file.readlines()
# 每一行自带换行符，要对每一行去除换行符
lines = [line.rstrip() for line in lines]
lines
file.close()

# 文件本身是一个迭代器：
file = open('script.py', 'r')
lines = [line.rstrip() for line in file]
lines
file.close()

# ====================拓展的列表解析语法
# 在列表解析中添加 if语句来收集满足条件的元素
file = open('script.py', 'r')
lines = [line.rstrip() for line in file if line[0] == 'p']
lines
file.close()

file = open('script.py', 'r')
lines = []
for line in file:
    if line[0] == 'p':
        lines.append(line.rstrip())

# 在列表解析中添加 for语句
a = [x + y for x in 'abc' for y in 'lmn']

a = []
for x in 'abc':
    for y in 'lmn':
        a.append(x + y) 
