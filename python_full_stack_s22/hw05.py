# # 1.请将列表中的每个元素通过 "_" 链接起来。
# users = ['大黑哥', '龚明阳', 666, '渣渣辉']
# users1 = [str(i) for i in users]
# print('_'.join(users1))


# # 2.请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
# v1 = (11, 22, 33)
# v2 = [44, 55, 66]
# for i in v1:
#     v2.append(i)
# print(v2)
#
# v1 = (11, 22, 33)
# v2 = [44, 55, 66]
# print(v2 + [i for i in v1])


# # 3.请将元组 v1 = (11,22,33,44,55,66,77,88,99)中的所有偶数索引位置的元素追加到新列表中
# v1 = (11,22,33,44,55,66,77,88,99)
# print([i for i in v1 if v1.index(i) % 2 == 0])


# # 4.将字典的键和值分别追加到key_list 和 value_list 两个列表中
# key_list, value_list = [], []
# info = {'k1':'v1','k2':'v2','k3':'v3'}
# for k, v in info.items():
#     key_list.append(k)
#     value_list.append(v)
# print(key_list)
# print(value_list)
#
# print([k for k in info.keys()])
# print([v for v in info.values()])


# # 5.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# # a. 请循环输出所有的key
# for k in dic.keys():
#     print(k)
#
# # b. 请循环输出所有的value
# for i in dic.values():
#     print(i)
#
# # c. 请循环输出所有的key和value
# for k,v in dic.items():
#     print(k,v)
#
# # d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)
#
# # *****
# # dic2 = {"k4":"v4"}
# # dic.update(dic2)
# # print(dic)
# # dic.setdefault("k4","v4")
# # print(dic)
#
#
# # e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
#
# # f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
#
# # g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0, 18)
# print(dic)


# 6.有如下字典,实现以下需求的内容
av_catalog = {
    "欧美": {
        "www.太白.com": ["很多免费的,世界最大的", "质量一般"],
        "www.alex.com": ["很多免费的,也很大", "质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "hao222.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}

# # 1)给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'。
# av_catalog['欧美']["www.太白.com"].insert(1, '量很大')
# print(av_catalog)

# 2)将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog["欧美"]["hao222.com"].pop()
# print(av_catalog)


# # 3)将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# ### av_catalog["日韩"]["tokyo-hot"][-1].upper()  # 是一个copy
# av_catalog["日韩"]["tokyo-hot"][-1]  = av_catalog["日韩"]["tokyo-hot"][-1].upper()
# print(av_catalog)


# # 4)给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"]['1048'] = ['一天就封了']
# print(av_catalog)


# # 5)删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# print(av_catalog)
# av_catalog['欧美'].pop('oldboy.com')
# print(av_catalog)

# # 6)给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog['大陆']['1024'][0] += '，可以爬下来'
# print(av_catalog)


# #### 7.请循环打印k2对应的值中的每个元素。info = {'k1':'v1','k2':[('alex'),('wupeiqi'),('oldboy')]}
# info = {'k1':'v1','k2':[('alex'),('wupeiqi'),('oldboy')]}
# for i in info['k2']:
#     print(i)


# ### 8.有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....}
# s = "k: 1|k1:2|k2:3  |k3 :4"
# s_list = s.split('|')
# dic = {}
# for i in s_list:
#     k, v = i.split(':')
#     key = k.strip()
#     value = int(v.strip())
#     dic[key] = value
# print(dic)
# # *****
# dic.setdefault()


# ### 9.有如下值 li= [11,22,33,44,55,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
# li= [11,22,33,44,55,77,88,99,90]
# dic = {"key1":[],"key2":[]}
# li = [11, 22, 33, 44, 55, 77, 88, 99, 90]
# for i in li:
#     if i > 66:
#         dic["key1"].append(i)
#     else:
#         dic["key2"].append(i)
# print(dic)


### 10.
# 1：输出商品列表，用户输入序号，显示用户选中的商品
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。
# goods = [
goods = [

    {"name": "电脑", "price": 1999},

    {"name": "鼠标", "price": 10},

    {"name": "游艇", "price": 20},

    {"name": "美女", "price": 998}
]

for i in goods:
    print(i['name'])





# 11. 看代码写结果(一定要先看代码在运行)
# v = {}
# for index in range(10):
#     v['users'] = index
# print(v)  # {'users': 9}




# # 用户输入一个数字,使用列表输出这个数字内的斐波那契数列
# n = int(input('请输入一个整数： '))
# a, b = 1, 1
# fab = []
# if n < 0:
#     fab = fab
# elif n == 1:
#     fab = []
# elif n == 2:
#     fab = [1, 1]
# else:
#     fab = [a, b]
#     for i in range(3, n + 1):
#         a, b = b, a+b
#         fab.append(b)
# print(fab)

# li = [1,1]
# num = int(input("请输入数字:"))
# flag = True
# while flag:
#     if li[-1] + li[-2] < num:
#         li.append(li[-1]+li[-2])
#     else:
#         flag = False
# print(li)


