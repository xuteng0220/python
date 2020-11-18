# # 问题？？？？？
#
# name = 'ryan'
# height = 169.8
# print(f'my name is {name}. my height is {round(height, 2)}')  # 显示是169.8，为何不是169.80？？？
#
# height = 169.73636
# print(round(height, 3))


# # # 1.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# l = [{'name': 'alex'}, {'name': 'y'}]
# # print(list(map(lambda x: x['name'] + '_sb', l)))
#
# def func(x):
#     x['name'] = x['name'] + '_sb'
#     return x
#
# new_l = map(func, l)
# print(list(new_l))

# ??????
# list(map(lambda x: {"name": x["name"]+"_sb"}, l))


# # 2.用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l = [dict(name='alex'), {'name': 'y'}]
# print(list(map(lambda x: {'name': x['name'] + 'sb'}, l)))


# # 3)用filter来处理,得到股票价格大于20的股票名字
#
# shares={
#  'IBM':36.6,
#  'Lenovo':23.2,
#  'oldboy':21.2,
#  'ocean':10.2,
#          }
# print(list(filter(lambda x: shares[x] > 20, shares)))


# # 4)有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。结果：list一下[9110.0, 27161.0,......]
# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
#
#
# # 并放在一个迭代器中 ?????
# ans = (i['shares'] * i['price'] for i in portfolio)
# print(ans)
# print(list(ans))
# for i in ans:
#     print(i)

# # 5)还是上面的字典，用filter过滤出单价大于100的股票。
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
#
# ans = filter(lambda x: x['price'] > 100, portfolio)
# print(list(ans))


# # 6)有下列三种数据类型，
# l1 = [1,2,3,4,5,6]
# l2 = ['oldboy','alex','wusir','太白','日天']
# tu = ('**','***','****','*******')
# # 写代码，最终得到的是（每个元祖第一个元素>2,第三个元素*至少是4个。）
# #  [(3, 'wusir', '****'), (4, '太白', '*******')]
# # 这样的数据。
# # '''
# ans_semi = zip(l1, l2, tu)
# # print(list(ans_semi))
# ans_final = filter(lambda x: x[0] > 2 and len(x[2]) >= 4, list(ans_semi)
# print(list(ans_final))


# # 7)有如下数据类型(实战题)：
# # 将l1按照列表中的每个字典的values从大到小进行排序，形成一个新的列表。
# l1 = [ {'sales_volumn': 0},
#        {'sales_volumn': 108},
#        {'sales_volumn': 337},
#        {'sales_volumn': 475},
#        {'sales_volumn': 396},
#        {'sales_volumn': 172},
#        {'sales_volumn': 9},
#        {'sales_volumn': 58},
#        {'sales_volumn': 272},
#        {'sales_volumn': 456},
#        {'sales_volumn': 440},
#        {'sales_volumn': 239}]
#
# ans = sorted(l1, key=lambda x: x['sales_volumn'], reverse=True)
# print(ans)


# # 3.有如下数据结构,通过过滤掉年龄大于16岁的字典
# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]
#
# ans = filter(lambda x: x['age'] <= 16, lst)
# print(list(ans))


# # 4.有如下列表,按照元素的长度进行升序
# lst = ['天龙八部','西游记','红楼梦','三国演义']
# ans = sorted(lst, key=lambda x: len(x))
# print(ans)


# # 5.有如下数据,按照元素的年龄进行升序
# lst = [{'id':1,'name':'alex','age':18},
#     {'id':2,'name':'wusir','age':17},
#     {'id':3,'name':'taibai','age':16},]
#
# ans = sorted(lst, key=lambda x: x['age'])
# print(ans)


# # 6.看代码叙说,两种方式的区别
# lst = [1, 7, 3, 5, 9, 12, 4]
# lst.reverse()  # Reverse *IN PLACE*
# print(lst)
#
# lst = [1, 7, 3, 5, 9, 12, 4]
# print(list(reversed(lst)))  # a new object
# print(lst)


# # *****************************************************************
# # 7.求结果(面试题)
# v = [lambda : x for x in range(10)]
# print(v)  #10个lambda函数地址
# print(v[0])  #第一个lambda函数的地址
# print(v[0]())  #9
# print(v[3]())
# print(v[9]())




# # *****************************************************************
# # 8.求结果(面试题)
# v = (lambda :x for x in range(10))
# print(v)#生成器地址
# print(v[0])#报错
# print(v[0]())#报错
# print(next(v))#生成器第一个函数的地址
# print(next(v)())#1


# # 9.map(str,[1,2,3,4,5,6,7,8,9]) 输出是什么? (面试题)
# map(str,[1,2,3,4,5,6,7,8,9])
# print(map(str,[1,2,3,4,5,6,7,8,9]))
# # 得到一个迭代器的地址
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))


# # 10.有一个数组[3, 4,1,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数的总和（上面数据的没有重复的总和为1+2=3)(面试题)
# lst = [3, 4, 1, 2, 5, 6, 6, 5, 4, 3, 3]
# ans = filter(lambda x: lst.count(x) == 1, lst)
# # print(list(ans))
# print(sum(ans))


# ***************************************************************
# # 1.求结果：（面试题，比较难）
# def num():
#     return [lambda x:i*x for i in range(4)]
#
# print([m(2)for m in num()])
