# # 1，使⽤循环打印以结果:
# for i in range(1, 6):
#     print('*' * (i * 2 - 1))

# # 2,使用while循环打印以下结果:
# i = 10
# while i > 0:
#     print('*' * i)
#     i -= 1


# # 3,写代码实现
# v1 = {"alex","wusir","taibai"}
# v2 = []
# # 循环让用户输入,如果用户输入的内容在v1中存在,就添加到v2中,如果v1中不存在就添加的v1中,用户输入Q退出程序
# while True:
#     s = input('请输入： ')
#     if s.upper() == 'Q':
#         break
#     if s in v1:
#         v2.append(s)
#     else:
#         v1.add(s)
# print(v1)
# print(v2)


# # 4.判断以下值那个能做字典的key ？那个能做集合的元素？
# -1 YES
# "" YES
# None YES
# [1,2] NO
# [] NO
# (1,2,3) YES
# ("1") YES
# (1,) YES
# {1,2,3,4} NO
# {"name":"alex","name1":"wusir"} NO

# # 5.is 和 == 的区别是什么?
# # is 判断两个变量的指向的地址是否相同
# # == 判断两个变量的值是否相同
# # is判断结果为True == 判断结果一定是True 而 == 判断为True is判断的结果不一定为True
# a = [1, 2, 3, 4, 5]
# a1 = [1, 2, 3, 4, 5]
# print(a is a1)
# print(a == a1)
# b = 'ryan'
# b1 = 'ryan'
# print(b is b1)
# print(b == b1)


# # 6.id的作用是什么?
# # id 查看变量指向的地址
# import ctypes
#
#
# a = 'ryan'
# print(a)
# print(id(a))
# get_value = ctypes.cast(id(a), ctypes.py_object).value
# print(get_value)

# # 7.看代码写结果并解释原因(以下看代码写结果,一定要自己先思考.在验证!)
# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = {'k1':'v1','k2':[1,2,3]}
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)

# # ***********************************************************************************
# # 10.看代码写结果并解释原因
# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = v1
# v1['k1'] = 'wupeiqi'
# print(v2["k1"] + v1["k1"])  # wupeiqiwupeiqi
# # 原因： v2 = v1 属于赋值操作，所以两个变量共用一个内存地址，无论通过哪个变量更改都会影响另一个变量
# # 赋值与切片比较
# x = ['k1', 'k2', ['k3', 'k4']]
# y = x
# z = x[:]
# x[0] = 'x1'
# print(x, y, z)
# x[2][0] = 'x3'
# print(x, y, z)


# # ***********************************************************************************
# 11.看代码写结果并解释原因
# v1 = '人生苦短，我用Python'
# v2 = [1, 2, 3, 4, v1]
# v1 = "人生苦短，用毛线Python"
# print(v2)
# 因为代码是从上到下执行的，所以输出[1,2,3,4,'人生苦短，我用Python']



# # ***********************************************************************************
# # # 12.看代码写结果,并解释原因
# info = [1, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
# info.append(9)
# print(userinfo)
# info = "题怎么这么多"
# print(userinfo)


# 13.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)
# ['不仅多，还特么难呢', 2, 3] [['不仅多，还特么难呢', 2, 3],
# ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3],
# ['不仅多，还特么难呢', 2, 3], ['不仅多，还特么难呢', 2, 3]]
# 改变元素,对应的源地址一样



# 14.看代码写结果并解释原因
# info = [1, 2, 3]
# userinfo = [info, info, info, info, info]
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)
# ['闭嘴', 2, 3] [['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3], ['闭嘴', 2, 3]]
# 浅拷贝,第二层元素可改变,源地址没改变


# 15.看代码写结果并解释原因
# info = [1, 2, 3]
# a = []
# for item in range(10):
#     a.append(info)
# info[1] = "是谁说Python好学的？"
# print(a)
# [[1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3], [1, '是谁说Python好学的？', 3]]
# 直接改


# 16.看代码写结果并解释原因
# data = {}
# for i in range(10):
#     data['user'] = i
# print(data) # {'user': 9}


# dict在内存中是怎么起作用的？****************************************************************

# 17.
data_list = []
data = {}
for i in range(10):
    data['user'] = i
    # print(id(data))
    data_list.append(data)
print(data_list)
# [{'user:9'},{'user:9'},{'user:9'},{'user:9'},{'user:9'},{'user:9'},{'user:9'},{'user:9'},{'user:9'},{'user:9'},]
# for 循环，每次添加给列表data_list,相当于浅拷贝，最后添加给列表时，直接修改


# 18.看代码写结果并解释原因
data_list = []
for i in range(10):
    data = {}
    data['user'] = i
    # print(id(data))
    data_list.append(data)
print(data_list)

# 19.
# 使用循环打印出一下效果：
#
#
#
# ```
#  *
#  **
#  ***
#  ****
# *****
#
# ```
# for i in range(6):
#     print(i*'*')
# #
#
#   ```
#   ****
#   ***
#   **
#   *
#   ```
# for i in range(4, 0, -1):
#     print(i*'*')
# #
#
#    ```
#      *
#     ***
#    *****
#   *******
#  *********
# *****************************************************
for i in range(1, 10, 2):
    print(i*'*')
#
#
# 20.敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.编程来完成敲七.给出⼀个任意的数字n.从1开始数.数到n结束.把每个数字都放在列表中, 在数的过程中出现7或
# 者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个
# '咣'
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
# user_input = input('请输入一个数字:')
# lst = []
# if user_input.isdecimal():
#     for i in range(1, int(user_input)+1):
#         if i % 7 == 0:
#             lst.append('咣')
#         else:
#             lst.append(i)
#     print(lst)