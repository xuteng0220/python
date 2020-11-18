# 2.用列表推导式做下列小题
# # 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# str_list = ['sjsye', 'sj', 'siwn', 'a', 'sajs']
# ans = [i.upper() for i in str_list if len(i) >= 3]
# print(ans)

# # 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
# ans = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 == 1]
# print(ans)

# # 求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1,2,3],[4,5,6],[7,8,9]]
# ans = [i[2] for i in M]
# print(ans)
#
# lst = [j for i in M for j in i if j % 3 == 0]
# print(lst)

# # 求出50以内能被3整除的数的平方，并放入到一个列表中。
# ans = [i ** 2 for i in range(51) if i % 3 == 0]
# print(ans)


# # 构建一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# ans = ['python' + str(i) + '期' for i in range(1, 11)]
# print(ans)


# # 构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# ans = [(i, i + 1) for i in range(6)]
# print(ans)


# # 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# ans = list(range(0, 19, 2))
# print(ans)


# # 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# ans = [i[1] + str(i[0]) for i in enumerate(l1)]
# # [i+str(l1.index(i)) for i in l1]
# print(ans)


# # 3.有以下数据类型：
# x = {'name':'alex','Values':[{'timestamp':1517991992.94,'values':100,},{'timestamp': 1517992000.94,
# 'values': 200,},
# {'timestamp': 1517992014.94,
# 'values': 300,},
# {'timestamp': 1517992744.94,
# 'values': 350},
# {'timestamp': 1517992800.94,
# 'values': 280}
# ],}
# # 将上面的数据通过列表推导式转换成下面的类型：[[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300],[1517992744.94, 350], [1517992800.94, 280]]
# ans = [[i['timestamp'], i['values']] for i in x['Values']]
# print(ans)
#
# ans1 = [[j for j in i.values()] for i in x['Values']]
# print(ans1)



# # 4.构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型）。
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
#
# t_shirt = [(i, j) for i in colors for j in sizes]
# print(t_shirt)


# # 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
# # l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
# num = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
# shape = ['spades', 'diamonds', 'clubs', 'hearts']
# l1 = [(i, j) for i in num for j in shape]
# print(l1)


# 6.简述一下yield 与yield from的区别
def func():
    l = [1, 2, 3]
    yield l
print(next(func()))

def func1():
    l1 = [1, 2, 3]
    yield from l1
print(next(func1()))

# # 7.看代码求结果（面试题）：
# v = [i % 2 for i in range(10)]  # 0-9之间的偶数的列表
# print(v)

v = (i % 2 for i in range(10))  # 是一个生成器地址
print(v)

# for i in range(5):
#      print(i)   # 0 1 2 3 4
# print(i) # 4













