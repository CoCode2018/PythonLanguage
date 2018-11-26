# 其他的核心对象类型

# 集合
# 唯一的不可变的对象的无需集合
# 通过调用内置set()函数创建集合
x = set('spam')
# 通过常量表达式创建集合
y = {'s', 'p', 'a', 'm'}
# 通过列表解析创建集合
z = {x * 2 for x in 'spam'}
# 集合对象可以做数学上集合运算 交、并、差
x & y
x | y
x - y

# 布尔型
# True False
# 实际上是定制以后以逻辑结果显示的整数1和0

1>2,1<2
bool('spam')
bool('0')
bool('')
bool([])
bool({})
bool(())
bool(0)
bool(None)

# None对象
# 占位符对象None

# 用来解决浮点数学的局限性和内在的不精确性
# 十进制小数
import decimal
decimal.Decimal()
# 分数
import fractions
fractions.Fraction()