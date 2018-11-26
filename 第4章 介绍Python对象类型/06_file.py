# 文件
# 文件对象是Python对电脑上外部文件操作的主要接口
# 文件对象虽然是核心对象类型，但是没有提供创建文件对象的常量表达式
# 创建文件对象需要调用内置的open()函数，并以字符串形式传递文件名和处理模式

f = open("data.txt", 'w')
f.write("Hello\n")
f.write('World\n')
f.close()

# 默认为 'r' 处理模式
f = open('data.txt')
text = f.read()
print(text)
print(text.split())