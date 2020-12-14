# # 1.看代码写结果
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v1.append(6)
# print(v1)
# print(v2)

# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v2[1][0] = 111
# v2[2][1] = 222
# print(v1)
# print(v2)

# v1 = [1,2,3,4,5,6,7,8,9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue        #排除掉了1，2，3，4，5
#     if 'k1' in v2:        #'k1'在v2中了 所以执行下一步 将item添加到v2中
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item ]    #当item为6的时候 创建一个新的字典 添加到v2空字典中
# print(v2)


# 4.简述赋值和深浅拷贝？
# 切片是浅拷贝，赋值比浅拷贝更弱
# 赋值就是共用同一个内存地址   浅拷贝：只拷贝第一层元素的内存地址，原列表修改了不可变数据类型，新开辟的列表不进行变动。
#  深拷贝：不可变数据类型公用（用于指向这些不可变数据类型的地址是不一样的），可变数据类型开辟了一个新的空间，对源数据进行改变，深拷贝的内容不会发生变化。



# from copy import deepcopy
# a = [1, 2, 3, [4, 5, 6]]
# b = a
# c = a[:]
# d = deepcopy(a)
# a[0] = 'x'
# a[3][0] = 'y'

# print(b)
# print(c)
# print(d)



# 5.看代码写结果
# import copy
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)
# print(v1 is v3)
# True
# True
# 6.看代码写结果
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)
# print(v1 is v3)
# False
# False
# 7.看代码写结果
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1[0] is v2[0])
# print(v1[0] is v3[0])
# print(v2[0] is v3[0])
# True
# True
# True

# 8.看代码写结果
# import copy
# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1[-1] is v2[-1])
# print(v1[-1] is v3[-1])
# print(v2[-1] is v3[-1])
# True
# False
# False

# 9.看代码写结果
# import copy
# v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
# v2 = copy.copy(v1)
# print(v1 is v2)
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
# False
# True
# True
# True
# True
# True

# 10.看代码写结果
# import copy
# v1 = [1,2,3,{"name":'太白',"numbers":[7,77,88]},4,5]
# v2 = copy.deepcopy(v1)
# print(v1 is v2)
# print(v1[0] is v2[0])
# print(v1[3] is v2[3])
# print(v1[3]['name'] is v2[3]['name'])
# print(v1[3]['numbers'] is v2[3]['numbers'])
# print(v1[3]['numbers'][1] is v2[3]['numbers'][1])
# False
# True
# False
# True
# False
# True
# 11.请说出下面a,b,c三个变量的数据类型。
# a = ('太白金星')   # 字符串
# b = (1,)          #元组
# c = ({'name': 'barry'})       #字典



# 12. 按照需求为列表排序：
# l1 = [1, 3, 6, 7, 9, 8, 5, 4, 2]
# 从大到小排序
# l1.sort(reverse=True)
# print(l1)
# 从小到大排序
# l1.sort()
# print(l1)
# 反转l1列表
# l1.reverse()
# print(l1)


# # 13.利用python代码构建一个这样的列表(升级题)：
# # [['_','_','_'],['_','_','_'],['_','_','_']]
# a = '_'
# b = [[a for i in range(3)] for j in range(3)]
# print(b)

# # 利用可变对象的赋值在
# l1=[]
# l2=[]
# for i  in  range(3):
#     l1.append("_")
#     l2.append(l1)
# print(l2)


# 14.看代码写结果：
# l1 = [1,2,]
# l1 += [3,4]
# print(l1)
# [1,2,3,4]
# # 15.看代码写结果：
# dic = dict.fromkeys('abc',[])
# dic['a'].append(666)
# print(dic)
# dic['b'].append(111)
# print(dic)


# # 16.l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除（不能一个一个删除）********************************************************
# l1 = [11, 22, 33, 44, 55]
# li=[]
# for i in l1:
#     li.append(i)
# for em in li:
#     if em % 2 == 0:
#         l1.remove(em)
# print(l1)

# # dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18} 请将字典中所有键带k元素的键值对删 ****************************************************************.
# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
# li=[]
# for i in dic:
#     li.append(i)
# for em in li:
#     if 'k' in em:
#         dic.pop(em)
#         # del dic[em]
# print(dic)




# # 17.完成下列需求：
# s1 = '太白金星'
# # 将s1转换成utf-8的bytes类型。
# s2=s1.encode('utf-8')
# print(s2)
# # 将s1转化成gbk的bytes类型。
# s3=s1.encode('gbk')
# print(s3)
# # b为utf-8的bytes类型，请转换成gbk的bytes类型。
# b = b'\xe5\xae\x9d\xe5\x85\x83\xe6\x9c\x80\xe5\xb8\x85'
# l1=b.decode('utf-8')
# l2=l1.encode('gbk')
# print(l2)


# # 18. 用户输入一个数字，判断一个数是否是水仙花数。
# # 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数,
# # 例如: 153 = 1**3 + 5**3 + 3**3
# msg = input('请输入一个数字')
# sum=0
# for i in msg:
#     sum=sum+int(i)**3
# # print(sum)
# if sum == int(msg):
#     print('是水仙花数')
# else:
#     print('不是水仙花数')


# 19. 把列表中所有姓周的⼈的信息删掉(此题有坑, 请慎重):
# lst = ['周⽼⼆', '周星星', '麻花藤', '周扒⽪']
# 结果: lst = ['麻花藤']


# 20.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌有多少. (选做题)
# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
# locals = {'沪':'上海', '⿊':'⿊龙江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
# 结果: {'⿊⻰江':2, '⼭东': 2, '上海': 1}



# dic={}
# for i  in cars:
#     # print(i[0])
#     if locals.get(i[0]):
#         dic[locals[i[0]]]=dic.get(locals[i[0]],0)+1
# print(dic)

