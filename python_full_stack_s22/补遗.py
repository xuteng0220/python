
# """
# # 需求
# 1. while循环提示 户输 : 户名、密码、邮箱(正则满 邮箱格式)
# 2. 为每个 户创建 个对象，并添加到 表中。
# 3. 当 表中的添加 3个对象后，跳出循环并以此循环打印所有 户的姓名和邮箱
# """


# class User: 
#     def __init__(self, name, pwd, email):
#         self.name = name
#         self.pwd = pwd
#         self.email = email

#     # def __str__(self):
#     #     return self.email


# class Account:
#     def __init__(self):
#         # 用户列表，数据格式：[user对象，user对象，user对象]
#         self.user_list = []
#         self.user_name_list = [user.name for user in user_list]
#         self.user_pwd_list = [user.pwd for user in user_list]
#         self.user_dict = dict(zip(self.user_name_list, self.user_pwd_list))


#     def login(self):
#         """
#         用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
#         :return:
#         """
#         name = input('enter your user name: ')
#         pwd = input('youe password: ')

#         if name in self.user_dict:
#             if pwd == self.user_dict[name]:
#                 print('logged in')
#             else:
#                 print('wrong password')
#         else:
#             print('unregistered user')
#             reply = input('do you want to register now? Y/N')
#             if reply.upper() == 'Y':
#                 self.register()


#     def register(self):
#         """
#         用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
#         :return:
#         """
#         while True:
#             name = input('select a user name: ')
#             if name in self.user_dict:
#                 print('this name is selected, try again')
#             else:
#                 pwd = input('enter your password: ')
#                 email = input('enter your email: ')
#                 self.user_list.append(User(name, pwd, email))
#                 print('registered')
#                 break

#     def change_password(self):
#         pass



#     def run(self):
#         """
#         主程序
#         :return:
#         """
#         self.login()


# if __name__ == '__main__':
#     obj = Account()
#     obj.run()




# class User:
#     def login(self):
#         print('登录')

#     def register(self):
#         print('register')

#     def save(self):
#         print('save')

# choose_dic = {
#     1: User.login,
#     2: User.register,
#     3: User.save,
# }

# while 1:
#     choose = input('请输入序号: \n1: 登录\n2: 注册\n3: 存储').strip()
#     obj = User()
#     choose_dic[int(choose)](obj)



# User.login(User())



# while else语句
count = 3
while count > 0:
    count = count - 1
    user = input("username:")
    pwd = input("password:")
    if user == 'alex' and pwd == 'alex3174':
        print('登陆成功！')
        break
    else:
        print(f"用户名或密码错误,还剩{count}次机会")
else:
    print("登陆次数太多，请稍后登陆！")