# 单引号和双引号是可以互换的，两种形式同样有效并返回想用类型的对象
'shurbbery', "shrubbery"
# 实现不使用反斜杠转义字符的情况下，在一个字符串中包含其余种类的引号

# 可以使用＋号连接不同的字符串
title = 'Meaning'+"of"+"Life"
title
# 并且Python自动在任意表达式中合并相邻的字符串常量
title = 'Meaning' "of" "Life"
title
# 相邻字符中添加，会生成元组
title = 'Meaning', "of", "Life"
title

# 转义序列
s = 'a\nb\tc'
print(s)
len(s)
s = 'a\0b\0c'
print(s)
s = '\001\002\x03'
print(s)

# raw字符串，抑制转移
file1 = open(r'C:\new\text.dat')
file2 = open('C:\\new\\text.dat')

# 三重引号，块字符串


# ======实际应用中的字符串
len('abc')
'abc' + 'edf'
'Ni' * 4

print('---------------------')
print('-' * 80)

myjob = 'hacker'
for c in myjob:
    print(c, end=' ')
'k' in myjob
'spam' in 'abcspamdef'

# 索引和分片
# python允许负偏移，一个字符的负偏移和这个字符串的长度相加后得到这个字符的正偏移值
# 负偏移：从结束处反向索引
s = 'spam'
s[0], s[-2]
s[1:3], s[1:], s[:-1]

B = '1101'
int(B, 2)
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1 : ] 