# 简述解释性语言和编译型语言的区别？
# 编译型语言:代码结束后,编码器会将其完全编译成另一种更贴近机器语言的文件,然后交给计算机执行
# 解释型语言:代码结束后,解释器会根据代码进行逐行的解释,这个过程边解释边执行
# 列举你了解的Python的数据类型？

# int str bool list tuple dict

# # 写代码，有如下列表，按照要求实现每一个功能。
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# # 1.计算列表的长度并输出
# print(len(l1))
#
# # 2.请通过步长获取索引为偶数的所有值，并打印出获取后的列表
# print(l1[::2])
#
# # 3.列表中追加元素"seven",并输出添加后的列表
# l1.append("seven")
# print(l1)
#
# # 4.请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# l1.insert(0, "Tony")
# print(l1)
#
# # 5.请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# l1[1] = "Kelly"
# print(l1)
#
#
# # 6.请将列表的第3个位置的值改成 “太白”，并输出修改后的列表
# l1[2] = "太白"
# print(l1)
#
#
# # 请将列表 l2=[1,“a”,3,4,“heart”] 的每一个元素追加到列表li中，并输出添加后的列表
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# l2 = [1, 'a', 3, 4, 'heart']
# print(l1 + l2)


# # 请将字符串 s = "qwert"的每一个元素添加到列表l1中，一行代码实现，不允许循环添加。
# # ????
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# s = "qwert"
# print(l1 + [i for i in s])
#
#
#
# # 请删除列表中的元素"ritian",并输出删除后的列表
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# # print(l1.pop(2))
# # print(l1)
# l1.remove("ritian")
# print(l1)


# # 请删除列表中的第2个元素，并输出删除元素后的列表
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# l1.pop(1)
# print(l1)
#
#
# # 请删除列表中的第2至第4个元素，并输出删除元素后的列表
# l1 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# del l1[1:4]
# print(l1)


# # 请用三种方法实现字符串反转 name = “小黑半夜三点在被窝玩愤怒的小鸟”（步长、while、for）
# name = '小黑半夜三点在被窝玩愤怒的小鸟'
# print(name[::-1])
#
#
# length1 = len(name)
# name1 = ''
# for i in range(length1-1, -1, -1):
#     name1 = name1 + name[i]
# print(name1)
#
# name2 = ''
# length2 = len(name) - 1
# while length2 >= 0:
#     name2 += name[length2]
#     length2 -= 1
# print(name2)


# # 写代码，有如下列表，利用切片实现每一个功能
# l1 = [1, 3, 2, "a", 4, "b", 5,"c"]
#
# # 通过对l1列表的切片形成新的列表 [1,3,2]
# print(l1[:3])
#
# # 通过对l1列表的切片形成新的列表 [“a”,4,“b”]
# print(l1[3:6])
#
# # 通过对l1列表的切片形成新的列表 [1,2,4,5]
# print(l1[::2])
#
# # 通过对l1列表的切片形成新的列表 [3,“a”,“b”]
# print(l1[1:7:2])
#
# # 通过对li列表的切片形成新的列表 [3,“a”,“b”,“c”]
# print(l1[1::2])
#
# # 通过对li列表的切片形成新的列表 [“c”]
# print(l1[-1])  # 是索引
# print(l1[-1:])  # 是切片
#
# # 通过对li列表的切片形成新的列表 [“b”,“a”,3]
# print(l1[5:0:-2])


# # 请用代码实现循环输出元素和值：users = [“武沛齐”,“景女神”,“肖大侠”] ，如：
# users = ['武沛齐', '景女神', '肖大侠']
# for i in users:
#     print(i)
#
#
# 写代码，有如下列表，按照要求实现每一个功能。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# # 1.将列表lis中的"k"变成大写，并打印列表。
# lis[2].upper()  # upper() return a copy
# lis[2] = 'K'
# print(lis)
#
# # 2.将列表中的数字3变成字符串"100"
# lis[1] = 100
# print(lis)
#
# # 将列表中的字符串"tt"变成数字 101
# lis[3][2][1][0] = 101
# print(lis)
#
# # 在 "qwe"前面插入字符串：“火车头”
# lis[3].insert(0, '火车头')
# print(lis)
#
# # 写代码实现以下功能
# # 如有变量 googs = [‘汽车’,‘飞机’,‘火箭’] 提示用户可供选择的商品：
# # 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
# googs = ['汽车', '飞机', '火箭']
# list_index = int(input('请输入选择商品的索引： '))
# print(googs[list_index])
#
#
# # 请用代码实现
# l1 = "alex"
# # 利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
# print('_'.join(l1))


# # 利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
# a = []
# for i in range(0, 101, 2):
#     a.append(i)
# print(a)
#
# b = [i for i in range(0, 101, 2)]
# c = list(range(0, 101, 2))
# print(b)
# print(c)
#
# # 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
# a = []
# for i in range(51):
#     if i % 3 == 0:
#         a.append(i)
# print(a)
#
# # 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
# b = []
# for i in range(51):
#     if i % 3 == 0:
#         b.insert(0, i)
# print(b)


# # 查找列表l1中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。
# l1 = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# a = []
# for i in l1:
#     i = i.strip()
#     if i[0] == 'a':
#         a.append(i)
# print(a)


# # 判断是否可以实现，如果可以请写代码实现。
# l1 = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry",), "wenzhou"]
# # 1.请将 “WuSir” 修改成 “武沛齐”
# l1[l1.index('WuSir')] = '武沛齐'
# print(l1)
#
# # 2.请将 (“ritian”, “barry”,) 修改为 [‘日天’,‘日地’]
# l1[3] = ['日天', '日地']
# print(l1)
#
# # 3.请将 88 修改为 87
# # tuple 是不可变对象
# # l1[1][2][1] = 87
#
#
# # 4.请将 “wenzhou” 删除，然后再在列表第0个索引位置插入 “文周”
# l1.pop()
# l1.insert(0, '文周')
# print(l1)



##################################
# ### 1
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(li)
# # 计算列表的长度并输出
# print(len(li))

# # 列表中追加元素"seven",并输出添加后的列表
# li.append("seven")
# print(li)

# # 请在列表的第2个位置前插入元素"Tony",并输出添加后的列表
# li.insert(1, "Tony")
# print(li)

# # 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1] = 'Kelly'
# print(li)

# # 请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中
# l2 = [1, "a", 3, 4, "heart"]
# li = li + l2
# print(li)

# # 将字符串s = "qwert"的每一个元素添加到列表li中
# s = 'qwert'
# for i in s:
#     li.append(i)
# print(li)

# # 删除列表中的元素"ritian",并输出添加后的列表
# i = li.index('ritian')
# li.pop(i)
# print(li)

# # 删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(1))
# print(li)

# # ******
# # 删除列表中的第2至4个元素，并输出删除元素后的列表
# for i in range(3, 0, -1):
#     li.pop(i)
# print(li)


# ### 2.li = [1, 3, 2, "a", 4, "b", 5,"c",["a","b","cc"]]
# li = [1, 3, 2, "a", 4, "b", 5,"c",["a","b","cc"]]
# l1 = li[0:3]  # [1, 3, 2]
# l2 = li[3:6]  # ['a', 4, 'b']
# l3 = li[0:8:2]  # [1, 2, 4, 5]
# l4 = li[1:7:2]  # [3, 'a', 'b']
# l5 = li[-2]  # 'c'
# # # ******
# # l6 = li[-4::-2]
# l7 = li[-1][::-1]  # ['cc', 'b', 'a']
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# print(l5)
# print(l6)
# print(l7)

# ### 3.lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][0] = "TT"
# print(lis)
# lis[-3][-2][-1][0] = lis[-3][-2][-1][0].upper()
# print(lis)
# lis[-3][-2][-1][1] = "100"
# print(lis)
# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][1] += 97
# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][1] = str(lis[-3][-2][-1][1])
# print(lis)

# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][2] = 101
# print(lis)
# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][2] += "01"
# print(lis)
# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[-3][-2][-1][2] = int(lis[-3][-2][-1][2])
# print(lis)

# ### 4.li = ["alex", "wusir", "taibai"]
# li = ["alex", "wusir", "taibai"]
# print("_".join(li))


# ### 5.li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)


# ### 6.利用for循环和range将100以内所有的偶数添加到一个新列表中。
# a = []
# for i in range(1, 100):
#     if i % 2 == 0:
#         a.append(i)
# print(a)
# print([i for i in range(1, 100) if i % 2 == 0])


# ### 7.利用for循环和range找出50以内能被3整除的数,并插入新列表
# print([i for i in range(50) if i % 3 == 0])

# ### 8.利用for循环和range从100 ~ -1，倒序打印。
# for i in range(100, -2, -1):
#     print(i)


# ### 9.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后在对列表的元素进行筛选，将能被4整除的数留下来。
# a = [i for i in range(100, 9, -1) if i % 2 == 0]
# b = [j for j in a if j % 4 == 0]
# print(a)
# print(b)


# ### 10.利用for循环和range，将1-30的数字中能被3整除的数改成* 依次添加到的列表当中
# print(['*' if i % 3 == 0 else i for i in range(1, 31)])



# ### 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# li_no_blank = [i.strip() for i in li]
# li_new = []
# for i in li_no_blank:
#     if i[0].upper() == 'A' and i[-1] == 'c':
#         li_new.append(i)
# print(li_new)
# print([i.strip() for i in li if i.strip()[0].upper() == 'A' and i.strip()[-1] == 'c'])


# # ### 12.敏感词语过滤程序
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# content = input("请输入评论内容:")
# li1 = []
# for i in li:
#     if i in content:
#         content = content.replace(i, '*'*len(i))
# li1.append(content)
# print(li1)


# ### 13.打印列表中的每个元素，若元素是一个列表，则其中的每个元素也要打印，且将字符串以小写打印
# # li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# # ***** 自己写
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in li:
#     if type(i) == list:
#         for j in i:
#             if type(j) == str:
#                 j = j.lower()
#                 print(j)
#             else:
#                 print(j)
#     elif type(i) == str:
#         i = i.lower()
#         print(i)
#     else:
#         print(i)



# ### 14. 斐波那契数列，到某一位置终止
# num = input("请输入数字:")
# li = [1, 1]
# a = 0
# for i in range(100):
#     if a < int(num):
#         a = li[i] + li[i + 1]
#         li.append(a)
#         if a > int(num):
#             li.pop()
# print(li)


# 递归实现斐波那契
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(2))
print(fib(10))










