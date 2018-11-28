# Python3提供next()内置函数来支持手动迭代
# 调用next(Obj)内置函数时会自动调用该对象的__next__()方法
f = open('script.py', 'r')
f.__next__()
f.__next__()
next(f)
next(f)
f.close()

# 当使用for循环时，可迭代对象会调用iter从而获得迭代器，这个迭代器中包含迭代所需要的next方法
L = [1, 2, 3]
K = (1, 2, 3)
# I is <list_iterator object at 0x7f5ae2d5a780>
I = iter(L)
I.__next__()
# O is <tuple_iterator object at 0x7f5ae2dbc748>
O = iter(K)
O.__next__()

# 文件对象不用调用iter()方法获得迭代器，因为文件对象本身就是迭代器
f = open('script.py', 'r')      # <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
iter_f = iter(f)    # <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
iter_f is f

# 列表等一些内置对象本身不是迭代器，需要调用iter()函数，获得迭代器
L = [1, 2, 3]
iter_L = iter(L)
iter_L is L
L.__next__()        # 'list' object has no attribute '__next__'
next(L)             # 'list' object is not an iterator
iter_L.__next__()
next(iter_L)

# 迭代工具　ＶＳ　手动迭代

L = [1, 2, 3]
for x in L:
    print(x ** 2, end=' ')

iter_L = iter(L)
while True:
    try:
        print(iter_L.__next__() ** 2, end=' ')
    except:
        break