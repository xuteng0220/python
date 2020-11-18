# # 2.写函数，接收n个数字，求这些参数数字的和。（动态传参）
# def cal_sum(a, *args):
#     s = a
#     for i in args:
#         s += i
#     return s
#
# print(cal_sum(1, 3, 4, 56, 10))


# # 3.读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b):
#     print(a, b)
# c = test5(b, a) # 20 10
# print(c) # None 无return，就返回None


# # 4.读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#    a=3
#    b=5
#    print(a,b)
# c = test5(b,a) # 3 5
# print(c) # None


# # 5.传入函数中多个列表和字典,如何将每个列表的每个元素依次添加到函数的动态参数args里面？如何将每个字典的所有键值对依次添加到kwargs里面
#################################### 看笔记？？？
# def func(*args, **kwargs):
#     for i in args:
#         print(i)
#     for j in kwargs:
#         print(j)
#     return
# a = [1, 2, 3, 4, 5]
# b = {'a': 1, 'b': 2}
# func(*a, **b)



# # 6.下面代码成立么?如果不成立为什么报错?怎么解决?
#
#  a = 2
#  def wrapper():
#      print(a)
#  wrapper()
# # 成立，局部命名空间没有就去全局命名空间找，结果是2
#
# a = 2
#  def wrapper():
#      a += 1
#      print(a)
# wrapper()
# # 报错，在局部命名空间修改一个变量，首先会认为局部命名空间已经定义了该变量，但在局部没找到，所以报错
#
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     inner()
#
# wrapper()
# # 成立，结果是1
#
# def wrapper():
#     a = 1
#     def inner():
#         a += 1
#         print(a)
#     inner()
#
# wrapper()
# # 报错，不能修改，除非声明nonlocal


# # 7.写函数,接收两个列表,将列表长度比较小的列表返回.
# def func(list1, list2):
#     return list1 if len(list1) < len(list2) else list2
#
# print(func([1, 2, 3], [6, 7, 8, 9, 10]))



# # 8.写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回. 例如 传入的可迭代对象为[1,'老男孩','宝元']返回的结果为’1_老男孩_宝元’'
# def func(iter_arg):
#     iter_list = [str(i) for i in iter_arg]
#     return '_'.join(iter_list)
#
# print(func((1, 2, 3, 4, 5, 's')))



# 看代码？？？
def fun(args,lst = []):
    for temp in args:
        if type(temp) != int and type(temp) != bool and type(temp) !=str and type(temp) != dict:
            fun(temp)
        elif type(temp) == dict:
            for i in temp:
                if type(i) != int and type(i) != bool and type(i) != str:
                    fun(i)
                else :
                    lst.append(str(i))
                if type(temp[i]) != int and type(temp[i]) != bool and type(temp[i]) !=str:
                    fun(temp[i])
                else:
                    lst.append(str(temp[i]))
        else:
            lst.append(str(temp))
    return  '_'.join(lst)


s = [1,2,[3,4,{1,5,9,8},[1],{5:6,(6,7):"ssdsadsa"}]]
print(fun(s))





