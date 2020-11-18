### 1.将今天的课上代码敲一遍，然后整理笔记
# a = 156
# # 二进制数
# print(bin(a))
# print(int('10011100', 2))
# name = 'absdefghijklmnopqrstuvwxyz'
# print(name[-2:])
# print(name[0:3:2])
# print(name[-2::-2])

# b = 'alex'
# print(b.upper())
# print(b)
# c = 'WUSIR'
# c = c.lower()
# print(c)
# d = 'asdf'
# print(d.startswith('a'))
# print(d.endswith('d'))
# e = 'asdfdafsafasa'
# f = e.count('a')
# print(f)
# g = '    adsff   '
# h = g.strip()
# print(g)
# print(h)

# i = '今天是个好日子'
# j = i.split('天')
# print(j)

# k = 'deabcfghijklmnopqrstuvwxyzde'
# l = k.replace('de', 'xt')
# l1 = k.replace('de', 'xt', 1)
# print(l)
# print(l1)

# a1 = '2345'
# a2 = a1.isdigit()
# print(a2)
#
# b1 = '12'
# b2 = b1.isdecimal()
# print(b2)
#
# c1 = '231asd中文'
# c2 = c1.isalnum()
#
# d1 = '中文'
# d2 = d1.isalpha()
# print(d2)

# for i in 'asdf':
#     print(i)
#
# for i in range(0, 100):
#     print(i)
#
# e1 = 'sadfssagg'
# print(len(e1))
# i = 0
# while i < len(e1):
#     i += 1
#     print(i)


# while input('请输入1或q， 1进入， q退出！>>>') != 'q':
#     content = input('请输入相加的数， 例如3+2， 按q退出>>>')
#     a = content.split('+')
#     print(int(a[0]) + int(a[1]))
# else:
#     print('退出成功！')




# goods = [{'name': '电脑', 'price': 1999},
#          {'name': '鼠标', 'price': 10},
#          {'name': '游艇', 'price': 20},
#          {'name': '美女', 'price': 998}
#          ]
# money, flag, sum_total, dic = 0, True, 0, {}
#
# # 进行充值
# while True:
#     money = input('请输入充值金额（Q/退出）: ')
#     if money.strip().isdecimal():
#         money = int(money)
#         print('充值成功，当前余额为%d' % money)
#         break
#     elif money.upper() == 'Q':
#         print('欢迎下次光临')
#         flag = False
#         break
#     else:
#         print('充值有误，请重新充值')
#
# # 开始购物
# my = {'money': money, 'shopping_car': [], 'flash': {}}
# while flag:
#     print('-' * 20)
#     for i in range(0, len(goods)):
#         print(i + 1, goods[i]['name'], goods[i]['price'])
#     number = input('请选择需要购买的商品（Q/退出；N/结算）: ')
#     if number.strip().isdecimal():
#         number = int(number)
#         if 0 < number < len(goods) + 1:
#             print('添加购物车成功')
#             # 添加选择的1个商品到列表shopping_car
#             my['shopping_car'].append(goods[number - 1]['name'] + ':' + str(goods[number - 1]['price']))
#             # 添加选择的1个商品到字典dic，记录商品name和price
#             dic[goods[number - 1]['name']] = goods[number - 1]['price']
#             # 添加选择的1个商品的价格到总计sum_total
#             sum_total += goods[number - 1]['price']
#             k, v = my['shopping_car'][-1].split(':')
#             # 把新添加到shopping_car的产品，加入到字典flash，记录商品name和数量，如果flash已有，数量+1，否则，数量=1
#             if k in my['flash']:
#                 my['flash'][k] = int(my['flash'][k]) + 1
#                 continue
#             my['flash'][goods[number - 1]['name']] = 1
#         else:
#             print('序号输入有误，请重新输入')
#     elif number.strip().upper() == 'Q':
#         if money > sum_total:
#             for k, v in my['flash'].items():
#                 print(k, v, dic[k])
#             print('此次消费%d元，账户余额为%d元' % (sum_total, money - sum_total))
#             for i in range(0, len(my['shopping_car'])):
#                 print((i + 1, my['shopping_car'][i]))
#             break
#         else:
#             print('账户余额不足')
#             print('欢迎下次光临')
#             break
#     elif number.strip().upper() == 'N':
#         while True:
#             if money > sum_total:
#                 print('已购清单如下：')
#                 for k, v in my['flash'].items():
#                     print(k, '数量：', v, '单价：', dic[k])
#                 change = input('是否结算？（Y/N)')
#                 if change.strip().upper() == 'Y':
#                     for k, v in my['flash'].items():
#                         # 打印名称、数量、价格
#                         print(k, v, dic[k])
#                     print('此次消费%d元，账户余额为%d元' % (sum_total, money - sum_total))
#                     for i in range(0, len(my['shopping_car'])):
#                         # 按加入的顺序打印加入购物车中的goods
#                         print(i + 1, my['shopping_car'][i])
#                     flag = False
#                     break
#                 elif change.strip().upper() == 'N':
#                     break
#                 else:
#                     print('输入有误，默认返回商品界面')
#             else:
#                 for i in range(0, len(my['shopping_car'])):
#                     print(i + 1, my['shopping_car'][i])
#                 choice = input('钱不够，请输入需要删除的商品（Q/退出）：')
#                 if choice.strip().isdecimal():
#                     choice = int(choice)
#                     if 0 < choice < len(my['shopping_car']) + 1:
#                         # a是name+price的字符串
#                         a = my['shopping_car'].pop(choice - 1)
#                         # 取name
#                         for i in my['flash']:
#                             if i in a:
#                                 my['flash'][i] = int(my['flash'][i]) - 1
#                                 sum_total -= int(dic[i])
#                         dic1 = my['flash'].copy()
#                         for i in dic1:
#                             if my['flash'][i] == 0:
#                                 my['flash'].pop(i)
#                 elif choice.strip().upper() == 'Q':
#                     if money > sum_total:
#                         print('此次消费%d元，账户余额%d元' % (sum_total, money - sum_total))
#                     else:
#                         print('账户余额不足')
#                         print('欢迎下次光临')
#                     break
#                 else:
#                     print('输入有误，请重新输入')
#     else:
#         print('输入有误，请重新输入')




# ### 2.name = "aleX leNb"
# name = "aleX leNb"
# print(name)
# print(name.strip())
# print(name.startswith("al"))
# print(name.endswith("Nb"))
# print(name.replace('l','p'))
# print(name.replace('l','p',1))
# print(name.split('l'))
# print(name.split('l',1))
# print(name.upper())
# print(name.lower())
# print(name.count('l'))
# print(name[0:4].count('l'))
# print(name[1])
# print(name[0:3])
# print(name[-2:])


# ### 3.s = "123a4b5c"
# s = "123a4b5c"
# s1 = s[0:3]
# s2 = s[3:6]
# s3 = s[0::2]
# s4 = s[1:6:2]
# s5 = s[-1]
# s6 = s[-3::-2]
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(s6)


# ### 4.使用while和for循环分别打印字符串s="asdfer"中每个元素。
# s = "asdfer"
# for i in s:
#     print(i)
# i = 0
# while i < len(s):
#     print(s[i])
#     i+=1


# ### 5.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"~
# s = "asdfer"
# for i in s:
#     print(s)


# ### 6.使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
# s = "abcdefg"
# for i in s:
#     print(i+"sb")


# ### 7.使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = "321"
# for i in s:
#     print("倒计时"+i+"秒")
# #     if i == "1":
# #         print("出发")
# print("出发")



# ### 8.实现一个整数加法计算器(两个数相加)：
# to_add = input('请输入两个数相加，比如1+2: ')
# a, b = to_add.split('+')
# print(int(a.strip()) + int(b.strip()))
#
# # user = input("请输入1或q，1进入，q退出！>>>")
# # while user != 'q':
# #     content = input("请输入相加的数，例如3+2,按q退出>>>")
# #     a = content.split("+")
# #     print(int(a[0])+int(a[1]))
# # else:
# #    print("退出成功！")


# ### 9.实现一个整数加法计算器（多个数相加）
# a = input('请输入1或q，1表示进入，q表示退出： ')
# while a.upper() != 'Q':
#     to_add = input('请输入需要相加的数字，比如1 2 3 4 5： ')
#     if to_add.upper() == 'Q':
#         break
#     s = 0
#     for i in to_add.split():
#         s += int(i)
#     print(s)
# else:
#     print('已退出')






# ### 10.计算用户输入的内容中有几个整数（以个位数为单位）
# a = input('请输入： ')
# count = 0
# for i in a.split():
#     if i.isdigit():
#         count += 1
# print(count)


# ### 11.计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
# j, s = -1, 0
# for i in range(1, 100):
#     j *= -1
#     if i != 88:
#         s = s + i * j
# print(s)


# # 12.选做题：写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。


while True:
    choice = input('请选择：')
    if choice == 'A':
        print('走大路回家')
        choice_a = input('公交车/步行：')
        if choice_a == '公交车':
            print('10分钟到家')
            break
        else:
            print('20分钟到家')
            break
    elif choice == 'B':
        print('走小路回家')
        break
    else:
        print('绕道回家')
        choice_c = input('游戏厅/网吧：')
        if choice_c == '游戏厅':
            print('一个半小时到家，爸爸在家，拿棍等你')
        else:
            print('两个小时到家，妈妈已经做好了战斗的准备')



# # ### 13.回文
#
# a = "十八到日本日到八十"
# if a[::-1] == a:
#     print("是回文")
# else:
#     print("不是回文")

