# 1.整理当天的笔记,将今天课上代码自己练习一下

# # 2.用户输入一个数字，判断一个数是否是水仙花数。
# # 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数, 例如: 153 = 13 + 53 + 3**3
# n = input('请输入： ')
# cube_sum = 0
# for i in n:
#     cube_sum += int(i) ** 3
# if cube_sum == int(n):
#     print('水仙花数')
# else:
#     print('不是水仙花数')


# # 3.请说出下面a,b,c三个变量的数据类型。
# a = ('太白金星')
# print(type(a))
# b = (1,)
# print(type(b))
# c = ({'name': 'barry'})
# print(type(c))

# # 4.按照需求为列表排序：
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# # 从大到小排序
# l1.sort(reverse=True)
# print(l1)
# # 从小到大排序
# l1.sort()
# print(l1)
# # 反转l1列表
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# l1.reverse()
# print(l1)


# # 5.看代码写结果：
# ××××××××××××××××××××××××××××××××××××××××
# dic = dict.fromkeys('abc', [])
# dic['a'].append(666)
# dic['b'].append(111)
# print(dic)

# # 6.完成彩票36选7的功能. 从36个数中随机的产生7个数. 最终获取到7个不重复的数据作为最终的开奖结果.
# from random import randint
# r_number = []
# i = 1
# while i < 8:
#     r = randint(1, 36)
#     if r in r_number:
#         continue
#     else:
#         r_number.append(r)
#         i += 1
# print(r_number)


# 7.字符串和字节转换
# # 将s1转换成utf-8的bytes类型。
# s1 = '太白金星'
# b1 = s1.encode('utf-8')
# b1_gbk = s1.encode('gbk')
# print(s1)
# print(b1)
# print(b1_gbk)
#
# # b为utf-8的bytes类型，请转换成gbk的bytes类型。
# b = b'\xe5\xa4\xaa\xe7\x99\xbd\xe6\x9c\x80\xe5\xb8\x85'
# s = b.decode('utf-8')
# print(s)
# b2 = s.encode('gbk')
# print(b2)


# # 8.把列表中所有姓周的⼈的信息删掉(升级题：此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# zhou = []
# for i in lst:
#     if i[0] == '周':
#         zhou.append(i)
# for j in zhou:
#     lst.remove(j)
# print(lst)


# # 9.⻋牌区域划分, 现给出以下⻋牌. 根据⻋牌的信息, 分析出各省的⻋牌持有量. (升级题)
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
# locals = {'沪':'上海', '⿊':'⿊龙江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京':'北京'}
# dic = {}
# for i in cars:
#     if locals[i[0]] in dic:
#         dic[locals[i[0]]] += 1
#     else:
#         dic[locals[i[0]]] = 1
# print(dic)
#
# dic = {}
# car = [i[0] for i in cars]
# for key in locals:
#     dic[locals[key]] = car.count(key)
# print(dic)
#
# jieguo = { }
# for i in locals.values():
#     jieguo[i] = 0
# for i in cars:
#     jieguo[locals[i[0]]] += 1
# print(jieguo)


# 10.⼲掉主播. 现有如下主播收益信息: zhubo = {'卢本伟':122000, '冯提莫':189999, '⾦⽼板': 99999, '吴⽼板': 25000000, 'alex': 126} 1. 计算主播平均收益值 2. ⼲掉收益⼩于平均值的主播 3. ⼲掉卢本伟
# zhubo = {'卢本伟':122000, '冯提莫':189999, '⾦⽼板': 99999, '吴⽼板': 25000000, 'alex': 126}
# print(zhubo)
# renshu = 0
# shouyi = 0
# for i in zhubo.values():
#     shouyi += i
#     renshu += 1
# avg_shouyi = shouyi / renshu
# gandiao = []
# for k, v in zhubo.items():
#     if v < avg_shouyi:
#         gandiao.append(k)
# for j in gandiao:
#     zhubo.pop(j)
# print(zhubo)
# # zhubo.pop('卢本伟')
# print(zhubo)