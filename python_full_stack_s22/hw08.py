# 1.有如下文件，a1.txt，里面的内容为：
"""老男孩是最好的学校，
全心全意为学生服务，
只为学生未来，不为牟利。
我说的都是真的。哈哈"""
# 分别完成以下的功能:
# # a,将原文件全部读出来并打印。
# f1 = open('hw08_a1', 'r', encoding='utf-8')
# content = f1.read()
# print(content)
# f1.close()

# # b,在原文件后面追加一行内容：信不信由你，反正我信了。
# f1 = open('hw08_a1', 'a', encoding='utf-8')
# f1.write("\n信不信由你，反正我信了")
# f1.close()

# # c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了
# f1 = open('hw08_a1', 'r+', encoding='utf-8')
# f1.read()
# f1.write("\n信不信由你，反正我信了")
# f1.close()


# # d,将原文件全部清空，换成下面的内容：
# """每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。"""
# f1 = open('hw08_a1', 'w', encoding='utf-8')
# f1.write("""每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。""")
# f1.close()


# 2.有如下文件，t1.txt,里面的内容为：
"""葫芦娃，葫芦娃，
一根藤上七个瓜
风吹雨打，都不怕，
啦啦啦啦。
我可以算命，而且算的特别准:
上面的内容你肯定是心里默唱出来的，对不对？哈哈
"""
# # 分别完成下面的功能：
# # a,以r的模式打开原文件，利用for循环遍历文件句柄。
# f1 = open('hw08_a2', mode='r', encoding='utf-8')
# for i in f1.read():
#     print(i)
# f1.close()
#
# # b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),并分析a,与b 有什么区别？深入理解文件句柄与 readlines()结果的区别。
# f1 = open('hw08_a2', mode='r', encoding='utf-8')
# for i in f1.readlines():
#     print(i)
# f1.close()


# c,以r模式读取‘葫芦娃，’前四个字符。
# with open('hw08_a2', mode='r', encoding='utf-8') as f1:
#     print(f1.read(4))

# d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# with open('hw08_a2', 'r', encoding='utf-8') as f1:
#       readline 读取第一行
#     l = f1.readline().strip()
#     print(l)


# with open('hw08_a2', 'rb') as f:  # 打开文件
#     # 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始,只能seek(offset,0)
#     first_line = f.readline()  # 取第一行
#     offset = -50  # 设置偏移量
#     while True:
#         """
#         file.seek(off, whence=0)：从文件中移动off个操作标记（文件指针），正往结束方向移动，负往开始方向移动。
#         如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
#         """
#         f.seek(offset, 2)  # seek(offset, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
#         lines = f.readlines()  # 读取文件指针范围内所有行
#         if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
#             last_line = lines[-1]  # 取最后一行
#             break
#         # 如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
#         # 所以off翻倍重新运行，直到readlines不止一行
#         offset *= 2
#     print('文件第一行为：' + first_line.decode())
#     print('文件最后一行为：' + last_line.decode())

# # e,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。
# with open('hw08_a2', 'a+', encoding='utf-8') as f1:
#     f1.write('\n老男孩教育')
#     f1.seek(0)
#     print(f1.read())


# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
"""apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3"""
# # 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
# a_list = []
# s = 0
# with open('hw08_a3', 'r', encoding='utf-8') as f1:
#     for i in f1.readlines():
#         a_dict = {}
#         name_price_amount = i.split()
#         a_dict['name'] = name_price_amount[0]
#         a_dict['price'] = int(name_price_amount[1])
#         a_dict['amount'] = int(name_price_amount[2])
#         a_list.append(a_dict)
#         s += int(name_price_amount[1]) * int(name_price_amount[2])
#         # k,v,j = i.split(" ")
#         # lst.append({"name": k,"price": int(v), "amount": int(j)})
#         # sum += int(v) * int(j)
# print(a_list)
# print(s)


# # 4.有如下文件：
# """alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。"""
# # 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
# with open('hw08_a4', 'r+', encoding='utf-8') as f1:
#     for line in f1.readlines():
#         if 'alex' in line:
#             line


未完成？？？

