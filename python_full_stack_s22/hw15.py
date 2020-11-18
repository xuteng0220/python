# # 1.请实现一个装饰器，限制该函数被调用的频率，如5秒一次（面试题）
# import time
#
#
# def wrapper(f):
#     def inner():
#         start_time = time.time()
#         time.sleep(5)
#         ret = f()
#         end_time = time.time()
#         print(f'调用func得等{end_time - start_time}秒')
#         return ret
#     return inner
#
# @wrapper
# def func():
#     print('func')
#
# func()



# # 2.请写出下列代码片段的输出结果：
#
# def say_hi(func):
#   def wrapper(*args,**kwargs):
#       print("HI")
#       ret=func(*args,**kwargs)
#       print("BYE")
#       return ret
#   return wrapper
#
# def say_yo(func):
#   def wrapper(*args,**kwargs):
#       print("Yo")
#       return func(*args,**kwargs)
#   return wrapper
#
# # 一层一层装饰
# @say_hi
# @say_yo
# def func():
#   print("ROCK&ROLL")
#
# func()
#
# # HI
# # Yo
# # ROCK&ROLL
# # BYE




# 3.编写装饰器完成下列需求:
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
# 启动程序后,呈现用户的选项为:
# 1,京东首页
# 2,京东超市
# 3,淘宝首页
# 4,淘宝超市
# 5,退出程序
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,只要输入一次京东账号和密码并成功,
# 则这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,只要输入一次淘宝账号和密码并成功,则这两个函数都可以任意访问.
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。
jingdong = {'username': 'ryan', 'password': 'ryan123'}
taobao = {'username': 'oligen', 'password': 'oligen123'}
auth_flag = {'jd': False, 'tb': False}


def auth(f):
    def inner():
        func_name = f.__name__[:2]
        if func_name == 'jd':
            dic = jingdong
        elif func_name == 'tb':
            dic = taobao
        if auth_flag[func_name]:
            f()
        else:
            print('请登录')
            username = input('请输入用户名：')
            password = input('请输入密码：')
            if username == dic['username'] and password == dic['password']:
                auth_flag[func_name] = True
                f()
            else:
                print('用户名/密码有误')
    return inner


@auth
def jd():
    print('京东首页')

@auth
def jd_market():
    print('京东超市')

@auth
def tb():
    print('淘宝首页')

@auth
def tb_market():
    print('淘宝超市')


while True:
    choice = input('请选择:1.京东首页，2.京东超市，3.淘宝首页，4.淘宝超市，5.退出程序 ')
    if choice == '1':
        jd()
    elif choice == '2':
        jd_market()
    elif choice == '3':
        tb()
    elif choice == '4':
        tb_market()
    elif choice == '5':
        break













# # 4.给l1 = [1,1,2,2,3,3,6,6,5,5,2,2]去重，不能使用set集合（面试题）
# l1 = [1,1,2,2,3,3,6,6,5,5,2,2]
# l1_unique = []
# for i in l1:
#     if i in l1_unique:
#         continue
#     else:
#         l1_unique.append(i)
# print(l1_unique)


# # # 5.用递归函数完成斐波那契数列（面试题）：
# def fib(n):
#     if n == 1:
#         ret = [1]
#     elif n == 2:
#         ret = [1, 1]
#     else:
#         ret = fib(n - 1)
#         ret.append(ret[-1] + ret[-2])
#     return ret
#
# print(fib(20))



# # 6.用户输入序号获取对应的斐波那契数字：比如输入6，返回的结果为8.
# def fib_num(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib_num(n-1) + fib_num(n-2)
#
# print(fib_num(7))





# ############################################################################################################
# ## 三级菜单
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
#
#
#
# def threeLM(dic):
#      while True:
#          for k in dic:print(k)
#          key = input('input>>').strip()
#          if key == 'b' or key == 'q':return key
#          elif key in dic.keys() and dic[key]:
#              ret = threeLM(dic[key])
#              if ret == 'q': return 'q'
#
#
# threeLM(menu)

