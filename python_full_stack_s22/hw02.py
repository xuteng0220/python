# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# # f or t or f and t and t or f  t
#
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# # not t and t or f and t and t or f  f

# print(3 > 4 or 4 < 3 and 1 == 1)  # f
# print(1 < 2 and 3 < 4 or 1 > 2)   # t
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)  # t
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)  # f
# print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # f
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # f

# print(8 or 3 and 4 or 2 and 0 or 9 and 7)  # 8
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)  # 4
#
# print(6 or 2 > 1)  # 6
# print(3 or 2 > 1)  # 3
# print(0 or 5 < 4)  # 0× # f
# print(5 < 4 or 3)  # 3
# print(2 > 1 or 6)  # 1× # t
# print(3 and 2 > 1)  # 1× # t
# print(0 and 3 > 1)  # 1× # 0
# print(2 > 1 and 3)  # 3
# print(3 > 1 and 0)  # 0
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)  # 2


# # 猜数字 73
#
# target = 73
# result = True
# while result:
#     guess = int(input("guess, please: "))
#     if guess < target:
#         print("your guess is less than the target, please try again")
#     elif guess > target:
#         print("your guess is larger than the target, please try again")
#     else:
#         print("yes")
#         result = False


# # 猜数字 73，只有三次机会
#
# target = 73
# result = True
# count = 0
# while result:
#     guess = int(input("guess, please: "))
#     if guess < target:
#         print("your guess is less than the target, please try again")
#     elif guess > target:
#         print("your guess is larger than the target, please try again")
#     else:
#         print("yes")
#         break
#     count += 1
#     if count == 3:
#         print("time")
#         break


num = 66
n = 3
while n:
    num1 = int(input("请输入猜测数字："))
    n -= 1
    if num1 == num:
        print("猜测正确！")
        break
    elif num1 > num:
        print("猜大了")
    else:
        print("猜小了")
else:
    print("你太笨了", end="")

# target = 66
# for i in range(3):
#     guess = int(input('请输入猜测数字：'))
#     if guess == target:
#         print('恭喜，猜中了')
#         break
# if guess != target and i == 2:
#     print("三次都没猜中")

# # 使用两种方法实现输出 1 2 3 4 5 6 8 9 10
# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)
#
#
# for i in range(1, 11):
#     if i == 7:
#         continue
#     print(i)


# # 求1-100的所有数的和
# i = 1
# sum_1 = 0
# while i < 101:
#     sum_1 += i
#     i += 1
# print(sum_1)
#
# sum_1 = 0
# for i in range(101):
#     sum_1 += i
# print(sum_1)


# # 输出 1-100 内的所有奇数
# for i in range(101):
#     if i % 2 == 1:
#         print(i)
#
# i = 1
# while i < 100:
#     print(i)
#     i += 2


# # 1-2+3-4+5 … 99的所有数的和
# sum1 = 0
# for i in range(1, 100):
#     sum1 = sum1 + (-1) ** (i-1) * i
# print(sum1)


# # 用户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
# password = 'abc123'
#
# times = 3
# result = True
# while result:
#     enter = input('please enter your password: ')
#     if enter == password:
#         print('yes')
#         break
#     else:
#         times -= 1
#         print('you have %s time(s) left' % times)
#     if times == 0:
#         break

password = 'abc123'
times = 3
while times:
    times -= 1
    in_pw = input('请输入密码：')
    if in_pw == password:
        print('登录成功')
        break
    else:
        if times == 0:
            print('输入有误，忘记密码')
        else:
            print(f'还有{times}机会')



# # 猜年龄游戏 要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
#
# age = 30
#
# for i in range(3):
#     guess = int(input('your guess: '))
#     if guess == age:
#         print('congratulation')
#         break


# 猜年龄游戏升级版 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如果猜对了，就直接退出
age = 30

times = 3
while times:
    times -= 1
    guess = int(input('输入猜测的年龄：'))
    if guess == age:
        print('猜中了')
        break
    else:
        if times == 0:
            yn = input('是否继续（y/n）：')
            if yn == 'y':
                times = 3
            else:
                print('游戏结束')
                break
        else:
            print(f'还有{times}机会')




# age = 30
#
# count = 3
# while count > 0:
#     print('you have %s chance(s) left' % count)
#     guess = int(input('enter your guess: '))
#     count -= 1
#     if guess == age:
#         print('congratulation')
#         break
#     while count == 0:
#         reply = input('do you want another 3 chances, please enter Y or N: ')
#         if reply == 'Y':
#             count = 3
#         elif reply == 'N':
#             break
#         else:
#             print('you enter is wrong, please enter again')
