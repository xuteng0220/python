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

# # *****
# # 8.看代码写结果并解释原因
# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = v1
# v1['k1'] = 'wupeiqi'
# print(v2["k1"] + v1["k1"])  # wupeiqiwupeiqi
# # 原因： v2 = v1 属于赋值操作，所以两个变量共用一个内存地址，无论通过哪个变量更改都会影响另一个变量


# # 9.看代码写结果并解释原因
# v1 = '人生苦短，我用Python'
# v2 = [1,2,3,4,v1]
# v1 = "人生苦短，用毛线Python"
# print(v2)
# # 原因：浅拷贝，"人生苦短，用毛线Python"这个字符串为新增内容，v1新开辟空间存储后更改指向，不影响原数据


# # 10.看代码写结果,并解释原因
# info = [1,2,3]
# userinfo = [info,info,info,info,info]
# info[0] = '不仅多，还特么难呢'
# print(info,userinfo)
# # 原因：浅拷贝，更改列表中的值，内存地址未发生变化



# # 11.看代码写结果,并解释原因
# dic1 = {"k1":5,"k2":10}
# dic2 = dic1.copy()
# dic2["k1"] = 1
# print(dic1["k1"] + dic2["k1"])
# # 原因：浅拷贝仅拷贝一层，dic2["k1"] = 1 是新开辟一块内容空间存储1

# # 12.念数字给出一个字典. 在字典中标识出每个数字的发音. 包括相关符号. 然后由用户输入一个数字. 让程序读出相对应的发音(单纯的打印即可,不考虑个十百)，例如: 7.5 输出: qi_dian_wu
# dic = {
# '0':'ling',
# '1':'yi',
# '2':'er',
# '3':'san',
# '4':'si',
# '5':'wu',
# '6':'liu',
# '7':'qi',
# '8':'ba',
# '9':'jiu',
# '.':'dian',
# }
#
# number = input('输入数字：')
# fayin = []
# for i in number:
#     fayin.append(dic[i])
# print('_'.join(fayin))


# 13.敲七游戏.从1开始数数.遇到7或者7的倍数要在桌上敲⼀下.编程来完成敲七.给出⼀个任意的数字n. 从1开始数 数到n结束.把每个数字都放在列表中, 在数的过程中出现7或者7的倍数(不包含类似于17,27，这种数).则向列表中添加⼀个'咣'
# 例如, 输⼊10 # lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
lst = []
n = int(input("请输入： "))
for i in range(1, n+1):
    if i % 7 == 0:
        lst.append('咣')
    else:
        lst.append(i)
print(lst)