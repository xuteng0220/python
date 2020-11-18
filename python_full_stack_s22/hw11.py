# # 1.请写出下列代码的执行结果：
# # 例一：
#
# def func1():
# 	print('in func1')
#
# def func2():
# 	print('in func2')
#
# ret = func1
#
# ret()  # in func1
#
# ret1 = func2
#
# ret1()  # in func2
#
# ret2 = ret
#
# ret3 = ret2
#
# ret2()  # in func1
#
# ret3()  # in func1
#
#
#
# # 例二：
#
# def func1():
#     print('in func1')
#
#
# def func2():
#     print('in func2')
#
#
# def func3(x, y):
#     x()
#     print('in func3')
#     y()
#
#
# print(111)  # 111
# func3(func2, func1)
# # in func2
# # in func3
# # in func1
#
# print(222)  # 222
#
#
# # 例三（选做题）：
#
# def func1():
#     print('in func1')
#
#
# def func2(x):
#     print('in func2')
#     return x
#
#
# def func3(y):
#     print('in func3')
#     return y
#
# ret = func2(func1)  # in func2    ret <= func1
# ret()  # in func1
# ret2 = func3(func2)  # in func3   ret2 <= func2
# ret3 = ret2(func1)   # in func2   ret3 <= func1
# ret3() # in func1




# # 看代码写结果：
# # 例四:
#
# def func(arg):
#     return arg.replace('苍老师', '***')
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
# run()  # Alex的女朋友***和大家都是好朋友
# data = run() # Alex的女朋友***和大家都是好朋友
# print(data) # None


# # 例五:
#
# data_list = []
#
# def func(arg):
#     return data_list.insert(0, arg)
#
# data = func('绕不死你')  # data <= ['绕不死你']
# print(data)  # None，注意：data <= data_list.insert(0. arg), 是list的方法insert被调用，就是函数+()，返回None（我猜是insert方法完成的工作已经在调用它的list里了，所以没别的东西返回）
# print(data_list)  # ['绕不死你']



# # 例六:
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀



# # 例七:
#
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀
# # 你好呀
# # 好你妹呀



# # 例八:
#
# def func():
#     return '大烧饼'
#
#
# def bar():
#     return '吃煎饼'
#
#
# def base(a1, a2):
#     return a1() + a2()
#
#
# result = base(func, bar)
# print(result) # 大烧饼吃煎饼


# # 例九:
#
# for item in range(10):
#     print(item)
#
# print(item) # 0 1 ... 9 9



# # 例十:
# 
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func() # 9



# # 例十一:
#
# item = '老男孩'
# def func():
#     item = 'alex'
#     def inner():
#         print(item)
#     for item in range(10):
#         pass
#     inner()
# func() # 9



# # 例十二:
#
# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
# print(func(1))  # [1]
# print(func(2))  # [1, 2]
# print(func(3))  # [1, 2, 3]



# # 例十三:
#
# name = '宝元'
# def func():
#     global name
#     name = '男神'
# print(name)  # 宝元
# func()
# print(name)  # 男神



# # 例十四:
#
# name = '宝元'
# def func():
#     print(name)
# func() # 宝元


# # 例十五:
#
# name = '宝元'
# def func():
#     print(name)
#     name = 'alex'
# func() # UnboundLocalError: local variable 'name' referenced before assignment



# # 例十六:
#
# def func():
#     count = 1
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     print(count)
#     inner()
#     print(count)
# func()
# # 1
# # 2
# # 2


# # 例十七:
# def extendList(val,list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# print('list1=%s'%list1)  # [10]
# list2 = extendList(123,[])
# print('list1=%s'%list2)  # [123]
# list3 = extendList('a')
# print('list1=%s'%list3)  # [10, 'a']
#
# # 注意！！！！！
# print('list1=%s'%list1)  # [10, 'a']
# print('list2=%s'%list2)  # [123]
# print('list3=%s'%list3)  # [10, 'a']



# 2.用你的理解解释一下什么是可迭代对象，什么是迭代器。
#可迭代对象:  有__item__方法
#迭代器:有__item__方法,__next__
# 3.使用while循环实现for循环的本质(面试题)
lst = [1, 2, 3, 4]
s = lst.__iter__()
print(s)
while True:
    try:
        print(s.__next__())
    except StopIteration:
        break







# # globals locals  global nonlocal
# # globals方法，Return the dictionary containing the current scope's global variables.
# print(globals())
# # Return a dictionary containing the current scope's local variables.
# print(locals())
#
# # 在局部调用globals locals
# def func():
#     a = 12
#     b = 20
#     print(locals())
#     print(globals())
#
# func()
#
# # global 简单来说就是让局部命名空间的变量能够使用全局命名空间中的变量
# a = 10
# def func():
#     global a
#     a = 20
#
# print(a)
# func()
# print(a)
#
#
# # nonlocal 可以理解为局部命名空间中的变量可以被外层使用
# def f1():
#     a = 1
#     def f2():
#         nonlocal a
#         a = 2
#     f2()
#     print('a in f1 : ', a)
#
# f1()
