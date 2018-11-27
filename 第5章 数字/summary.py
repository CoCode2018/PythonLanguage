"""
    第5章 数字

1.Python中数字并不是一个真正的对象类型而是一组类似对象类型的分类
    (整数、浮点数、复数、十进制小数、分数、集合、布尔类型、内置函数及模块)
2.整数：
    无穷精度
    有二进制、八进制、十进制、十六进制等表示方法，并且不论用那种方式表示整数，在内存中都只有一个整数对象，它们仅仅是特定值的不同语法表示而已
3.浮点数
    自动启用浮点数运算规则
    双精度，与构建Python解释器的C编译器给定的双精度相同
4.复数
    常量创建或者调用内置complex(real,img)函数创建
    内部通过一对浮点数表示，启用复数的运算法则
"""

"""
处理数字对象的工具
    1.表达式操作符
    2.内置数学函数
    3.公用模块
    4.特定类型的方法
"""

# ===========内置数学工具
# =====内置函数
# 计算幂
pow()
# 计算绝对值
abs()
# =====内置模块
# math、cmath、random

# ==========其他数字类型
# =====小数数字类型
# 固定精度的浮点数
print(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')

import decimal
decimal.getcontext().prec = 4
#　小数上下文管理器
with decimal.localcontext() as ctx:
    ctx.prec = 5
    decimal.Decimal('1.00') / decimal.Decimal('3.00')

# =====分数类型，明确保留一个分子、分母
import fractions
x = fractions.Fraction(1, 3)
print(x)
y = fractions.Fraction('1.25')
print(y)
(2.5).as_integer_ratio()
z = fractions.Fraction(*(2.5).as_integer_ratio())

# =====集合
# 集合只能包含不可变对象

# =====布尔型
# bool:  True/False

# 数字拓展
# NumPy