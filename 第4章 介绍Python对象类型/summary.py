"""
    第4章 介绍Python对象类型

1.介绍对象类型以及这些对象可以做的事情，对象无非是内存中的一部分，包含数值和相关操作的集合(属性和行为)
2.在Python中一切皆是对象
3.Python程序可以分解为模块、语句、表达式、对象：
    程序有模块构成
    模块包含语句
    语句包含表达式
    表达式创建并处理对象
4.探讨编程过程中使用的内置对象和表达式以及基本的操作(行文)
    数字：并不是一个标准的对象类型，而是一些类似的对象类型的集合(整数、浮点数、复数、固定精度的十进制数、分数、集合)
    字符串：
    列表：
    字典：
    元组：
    文件：
    其他核心类型
5.Python提供强大的对象类型作为语言的组成部分，在开始解决问题之前不用先去编写对象的实现。内置对象类型不仅让程序编写变得简单而且更强大和更高效
    1.内置对象类型使程序更容易编写
    2.内置对象是可拓展的组件
    3.内置对象往往比定制的数据结构更有效率
    4.内置对象是语言的标准的一部分
6.核心的数据对象类型
    在Python程序中处理的每一样东西都是一种对象
    核心的数据类型由Python语言内部高效创建，其他类型的对象可以通过模块导入，并且都有各自的行为
        数字
        字符串
        列表
        元组
        字典
        集合
        文件
        其他类型            类型、None、布尔型
        编程单元类型        函数、模块、类
        与实现相关的类型    编译的代码堆栈跟踪
    这些核心的对象类型都有固定的常量(Iiteral)表达式来创建生成这些对象，其他的对象通过调用模块中的方法进行创建
    Python中没有类型声明，运行的 （表达式的语法）决定了创建和使用的对象的类型，对象一旦创建便和对应的操作集合绑定了
7.如何破坏代码的灵活性
    Python3中类型和类已经结合起来了，在代码中进行特定类型检测实际上破坏了它的灵活性，即限制它只能使用一种类型工作，没有类型检测代码也许能使用整个范围的类型工作
    在Python中我们编写对象接口(对象支持的操作)，而不是编写对象。不关注特定的类型意味着代码能够自动的适应它们中的很多类型：
        任何具有兼容性的接口都能工作，不管它是什么类型，因此尽管支持类型检测却很少使用，这会破坏代码的灵活性
8.用户自定义类
    之所以叫做面向对象模型是因为一个类中的函数总有一个隐含的对象
9.我们学过的对象仅仅是对象而已，并不一定是面向对象。面向对象是一种往往要求继承和Python类声明的概念

"""


# ==========检查所处理对象的类型
L = [x for x in range(3)]
# 1.
if type(L) == type([]):
    print('Yes')
# 2.
if type(L) == list:
    print("Yes")
# 3.
if isinstance(L, list):
    print("Yes")

# ==========用户自定义类
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split(' ')[-1]
    def giveRaise(self, percent):
        self.pay += self.pay * percent
    