# # *****************************************************
#
# login_dic = {'username': None, 'flag': False}
#
# # 装饰器
# def auth(f):
#     def inner(*args, **kwargs):
#         if login_dic['flag']:
#             return f()
#         else:
#             return login()
#         return inner
#
#
# @auth
# def index():
#     print(f'这是{login_dic["username"]}的主页')
#     return
#
# def login():
#     print('这是一个登录页面')
#     user = input('username:')
#     pwd = input('password:')
#     if user == 'baoyuan' and pwd == 'baoyuan123':
#         login_dic['flag'] = True
#         login_dic['username'] = user
#         return '登录成功'
#     else:
#         return '用户名密码有误'
#
# @auth
# def comment():
#     if login_dic['flag'] == True:
#         return f'这是{login_dic["username"]}的评论'
#
# while not login_dic['flag']:
#     if comment() is None:
#         break
#     else:
#         print(comment())
#
#
# index()
#
# # *****************************************************


# # 看代码写结果：
# def wrapper(f):
#     def inner(*args,**kwargs):
#         print(111)
#         ret = f(*args,**kwargs)
#         print(222)
#         return ret
#     return inner
#
# def func():
#     print(333)
#
# print(444)  # 444
# func()  # 333
# print(555)  # 555


# # 4.编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里’。
#
# def def_func(f):
#     def inner():
#         print(f'每次执行被装饰函数之前都得先经过这里')
#         ret = f()
#         return ret
#     return inner
#
# @def_func  # func = def_func(func)
# def func():
#     print(333)
#
# func()


# # 5.为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# def wrapper(f):
#     def inner(a, b):
#         ret = f(a, b)
#         ret += 100
#         return ret
#     return inner
#
#
# @wrapper
# def func(a, b):
#     return a + b
#
# post_ret = func(7, 11)
# print(post_ret)


# # 6.请实现一个装饰器，通过一次调用使被装饰的函数重复执行5次。
#
# def wrapper(f):
#     def inner(a, b):
#         for i in range(5):
#             ret = f(a, b)
#         return ret
#     return inner
#
#
# @wrapper
# def func(a, b):
#     print(a + b)
#
#
# func(1, 2)



# 7.请实现一个装饰器，每次调用函数时，将被装饰的函数名以及调用被装饰函数的时间节点写入文件中。



import time

call_fun_log = []
def wrapper(f):
    def inner():
        struct_time = time.localtime()
        call_time = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)

        call_fun_log.append((f.__name__, call_time))
        f()
    return inner


@wrapper
def func():
    print('函数被调用了一次')

func()
print(call_fun_log)

