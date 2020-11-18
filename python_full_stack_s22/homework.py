# # 定义一个圆类，属性为r，方法1.计算周长，2.计算面积
# import math
#
#
# class Circle:
#
#     def __init__(self, r):
#         self.r = r
#
#     def zhouchang(self):
#         return 2 * self.r * math.pi
#
#     def mianji(self):
#         return math.pi * self.r * self.r
#
#
# yuan1 = Circle(5)
# yuan2 = Circle(10)
#
# print(yuan1.zhouchang())
# print(yuan2.mianji())


# # 用户类，属性：用户名、密码，方法：修改密码；登录成功，才能创建用户对象
# class User:
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def change_password(self):
#         print("please enter your password")
#         pw = input()
#         if pw == self.password:
#             print("please enter your new password")
#             new_pw = input()
#             self.password = new_pw
#         else:
#             print("your password is wrong")
#
#
# user1 = User("ryan", "123456")
# user1.change_password()
# print(user1.password)


# 人狗大战
class Dog:

    def __init__(self, name, gender, blood, attack, action, skill, tool):
        self.name = name
        self.gender = gender
        self.blood = blood
        self.attack = attack
        self.action = action
        self.skill = skill
        self.tool = tool





















