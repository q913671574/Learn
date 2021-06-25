from decimal import Decimal
from operator import itemgetter
from statistics import mean
##yield 的使用
#print("yield 的使用")
# def foo(num):
#     print("starting...")
#     while num < 10:
#         num = num + 1
#         yield num
#
#
# result = foo(0)
# print(next(result))
# print("下一个是：")
# print(next(result))
#
#
# # for i in foo(1):
# #     print(i)
#


# def multiply(x):
#     return x * x
#
# def add(x):
#     return x + x
#
# funcs = [multiply, add]
#
# for i in range(6):
#     value = map(lambda x: x(i), [multiply, add])      #计算 [x^2, x+x]
#     print(list(value))

##循环计算  1*2*3*4的值
#print("循环计算  1*2*3*4的值")
# from functools import reduce
# product = reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
# print(product)

from collections import Counter, namedtuple, defaultdict
from functools import wraps

##装饰器
#print("装饰器")
# from typing import Type, List, Any
# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#     return with_logging
# @logit
# def addition_func(x):
#     """Do some math."""
#     return x + x
# result = addition_func(4)
# print(result)


#同时返回多个值
# print("同时返回多个值")
# def profile():
#     name = "Danny"
#     age = 30
#     return name, age
#
# result = profile()
# print(result)
#
# #列表的引用
# a = ['111']
# b=['111']
# c=a
# print(id(a))
# print(id(b))
# print(id(c))

##使用Counter计算各个键对应几个值
# print("使用Counter计算各个键对应几个值")
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# favs = Counter(a for a, colour in colours)
# print(favs)

# Anima = namedtuple('Animal', 'name age type')
# #Anima.age = "77"
# z = Anima("a", "2", "dog")
# print(z.type)
#
# my_list = ['apple', 'banana', 'grapes', 'pear']
# for name, value in enumerate(my_list, 1):
#     print(name, value)


#舍去首位，计算中间数据的平均值
# print("舍去首位，计算中间数据的平均值")
# grades = [20,30,40,50,60]
# def drop_first_last(grades):
#     first, *middle, last = grades  # 将多个变量存储在一个变量中，如middle，其永远是列表类型
#     return mean(middle)
# avg = drop_first_last(grades)
# print(avg)
#
# rows = [{'fname': 'John', 'lname':'cleese', 'uid':1001},
#         {'fname':'Big', 'lname':'Jones', 'uid':1004}]
# print(type(rows[1]))
# rows_by_fname = sorted(rows, key = itemgetter('fname'))
# print(rows_by_fname)

#从数据序列中提取所需数据
# print("从数据序列中提取所需数据")
# mylist = [1, 4, -5, -20, -7, 2, 3, -1]
# print([n for n in mylist if n > 0])          #筛选出大于0的数据
# print([n if n > 0 else 0 for n in mylist])   #筛选出大于0的数据并且小于0的数据用0替换掉。输出：[1, 4, 0, 0, 0, 2, 3, 0]
# #使用生成器表达式迭代产生过滤元素
# pos = (n for n in mylist if n > 0)
# for x in pos:
#     print(x)

#过滤规则比较复杂需要处理一些异常或者其他负责情况时，可以将过滤代码放到一个函数中，然后使用内建的filter()函数
# print("过滤器")
# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
# ivals = list(filter(is_int, values))
# print(ivals)                                #输出：['1', '2', '-3', '4', '5']
# from itertools import compress
# more5 = [True, False, False, True]
# print(list(compress(values, more5)))        #输出：['1', '-']

#命名元组
# print("命名元组")
# from collections import namedtuple
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2012-10-19')
# print(sub)          #输出：Subscriber(addr='jonesy@example.com', joined='2012-10-19')
# print(sub[0])       #输出：jonesy@example.com
# print(sub.addr)     #输出：jonesy@example.com


# s = ('ACME', 50, 123.45)
# print(list(','.join(str(x)) for x in s))    #输出：['A,C,M,E', '5,0', '1,2,3,.,4,5']

#同时遍历多个字典
# print("同时遍历多个字典")
# from collections import ChainMap
# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
# c = ChainMap(a,b)
# print(c['x'])               # Outputs 1 (from a)
# print(c['y'])               # Outputs 2 (from b)
# print(c['z'])               # Outputs 3 (from a)

#正则表达式
# print('正则表达式')
# import re
# a=re.finditer(r'[aeiou]', 'I love FishC.com!')
# for n in a:
#     print(n)
#
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
# print(datepat.match('11/27/2012abcdef'))
# print(datepat.match('11/27/2012'))
#
# from calendar import month_abbr
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     print(m.group(0), m.group(1), m.group(2), m.group(3))
#     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
#
# print(datepat.sub(change_date, text))

#大小写替换
# def matchcase(word):
#     def replace(m):
#         text = m.group()
#         if text.isupper():
#             return word.upper()
#         elif text.islower():
#             return word.lower()
#         elif text[0].isupper():
#             return word.capitalize()
#         else:
#             return word
#     return replace
#
# print(matchcase("IoDc"))

#带有变量的字符串的格式化输出
# s = '{name} has {n} messages.'
# name = 'Guido'
# n = 37
# s.format_map(vars())
# print(s)


#多映射值字典类型
# d = {}
# d.setdefault('b', []).append(1)
# print(d['b'])
# print(type(d['b']))
# d.setdefault('b', []).append(3)
# print(d['b'])


# a = Decimal('2.1')
# b = Decimal('4.2')
# print(a)
# print((a+b) == Decimal('6.3'))
#
# x = 1234.56789
# print(format(x, '^10,.1f'))

#复数
# a = complex(2, 4)       #第一个参数2是实部，第二个参数4是虚部
# b = 3 - 5j
# print(a * b)    #复数乘法

#分数模块
# from fractions import Fraction
# a = Fraction(5, 4)  # 第一个参数是分子，第二个参数是分母
# b = Fraction(7, 16)
# print(a + b)  # 输出27/16
# c = a * b
# print(c)  # 输出35/64
# print(c.numerator)  # 输出35， 获取分子
# print(c.denominator)  # 输出64， 获取分母
#
# print(c.limit_denominator(8))
# print(c.limit_denominator(16))
# print(c.limit_denominator(20))
# print(c.limit_denominator(50))

#数组(矩阵之间的运算)
# import numpy as np
# grid = np.zeros(shape=(3, 3), dtype = float)
# print(grid)
#
# d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#
# print(d[1])
# print(d[:, 1])
# #列表的运算操作,普通列表只能进行列表之间的'+'，或者与整数之间的'*'操作
# li = [4, 3, 2, 1]
# l = [0]
# print(li * 2)               #输出：[4, 3, 2, 1, 4, 3, 2, 1]
# print(li + l +  li * 2)     #输出：[4, 3, 2, 1, 0, 4, 3, 2, 1, 4, 3, 2, 1]

#随机数random模块，手动设置种子，三次输出的随机数一样
# import random
# random.seed(10)
# print(random.random())
# random.seed(10)
# print(random.random())
# random.seed(10)
# print(random.random())
#

#基本的日期与时间转换
# from datetime import timedelta, datetime
# a = timedelta(days=2, hours=6, minutes=1, seconds=1)    #创建一个时间变量，天数=2，小时数=6，分钟数=1，秒钟数=1
# b = timedelta(hours=4.5)
# c = a + b                                               #两个时间变量相加
# print(c.days)                                           #输出时间变量的天数或者秒数
# print(c.seconds)
# print(c.total_seconds()/3600)

# d = datetime.now()                                      #获取当前日期与时间
# print(d)
# text = '2012-09-20'
# y = datetime.strptime(text, '%Y-%m-%d')                 #将字符串日期 格式化输出
# print(y)


#迭代器
# items = [1, 2, 3]       #创建一个列表
# it = iter(items)        #将列表转化为一个迭代器传给it
# print(next(it))



#在自定义类上实现__reversed__()方法来实现反向迭代
#自己定义一个reversed同名的内部方法(并非系统内置)，让外部调用
# class Countdown:
#     def __init__(self, start):
#         self.start = start
#
#     #常规迭代方法，倒数输出数字
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#     #反向迭代方法，正数输出数字
#     def __reversed__(self):
#         n = 1
#         while n<= self.start:
#             yield n
#             n += 1
# for rr in reversed(Countdown(30)):
#     print(rr)
#
# print('Done!')
# for rr in Countdown(30):
#     print(rr)
#查看可供Countdown调用的方法
# print(dir(Countdown))

#使用itertools.islice()方法对迭代器和生成器进行切片操作
# import itertools
# #创建一个生成器
# def count(n):
#     while True:
#         yield n
#         n += 1
# c = count(0)
# #c[10:20]        #会报错
# for x in itertools.islice(c, 10, 20):
#     print(x)
# print('Done!')

#略过文本开头的注释
# fl = "" \
#      "# User Database" \
#      "# Note that this file is consulted directly only when the system is running" \
#      "# in single-user mode. At other times, this information is provided b" \
#      "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false" \
#      "root:*:0:0:System Administrator:/var/root:/bin/sh" \
#      ""
# from itertools import dropwhile
# for line in dropwhile(lambda line: line.startswith('#'), fl):
#     print(line, end='')

#对集合中元素进行配列组合
# print("排列组合")
# items = ['a', 'b', 'c']
# from itertools import permutations
# #permutations它接受一个集合并产生一个元组序列，序列中每个元组由集合中所有元素的一个可能排列组成，无重复数据的排列('a', 'a', 'a')
# for p in permutations(items):    #num表示指定长度的排序
#     print(p)
# #itertools.combinations() 可得到输入集合中元素的所有的组合
# from itertools import combinations
# for c in combinations(items, 2):  #获得num个数据的所有组合
#     print(c)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)
print('Short is done.')
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)



