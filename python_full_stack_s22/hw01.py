### 1.简述变量命名规范
# - 小写字母、下划线开头
# - 不能用数字开头
# - camalCase
# - PascalNameingConvention 不推荐，一般用在类变量名
# - uderline_name_convention
# - 避免使用python关键字
# ****
# 不能使用中文和拼音
# 变量名要有意义


# ### 2.name = input(“>>>”) name变量是什么数据类型通过代码检测
# name = input('>>>')
# print(type(name))


# ### 3.if条件语句的基本结构？
# if expression1:
#     statement1
# elif expression2:
#     statement2
# else:
#     statement


# ### 4.用print打印出下面内容：
# msg = """
# ⽂能提笔安天下,
# 武能上马定乾坤.
# ⼼存谋略何⼈胜,
# 古今英雄唯是君.
# """
# print(msg)


# ### 5.利用if语句写出猜大小的游戏：
# num = 73
# user = int(input("请输入您猜测的数字: "))
# if user > num:
#     print('大了')
# elif user < num:
#     print('小了')
# else:
#     print('猜中了')



# ### 6.提⽰⽤户输入他的年龄, 程序进⾏判断.
# # 1.10以下 ⼩屁孩
# # 2.10-20 青春期叛逆的⼩屁孩
# # 3.20-30 开始定性, 开始混社会的⼩屁孩⼉
# # 4.30-40 老⼤不⼩了, 赶紧结婚⼩屁孩⼉.
# # 5.40-50 家⾥有个不听话的⼩屁孩⼉.
# # 6.50-60 ⾃⼰⻢上变成不听 话的老屁孩⼉.
# # 7.60-70 活着还不错的老屁孩⼉.
# # 8.70-90 ⼈⽣就快结束了的⼀个老屁孩⼉.
# # 9.90++ 再⻅了这个世界
# user = int(input("请输入你的年龄："))
# if user < 10:
#     print('小屁孩')
# elif user <= 20:
#     print('青春期叛逆的⼩屁孩')
# elif user <= 30:
#     print('开始定性, 开始混社会的⼩屁孩⼉')
# elif user <= 40:
#     print('老⼤不⼩了, 赶紧结婚⼩屁孩⼉.')
# elif user <= 50:
#     print('家⾥有个不听话的⼩屁孩⼉.')
# elif user <= 60:
#     print('⾃⼰⻢上变成不听 话的老屁孩⼉.')
# elif user <= 70:
#     print('活着还不错的老屁孩⼉.')
# elif user <= 90:
#     print('⼈⽣就快结束了的⼀个老屁孩⼉.')
# else:
#     print('再⻅了这个世界')


# ### 7.单行注释以及多行注释表示方式
# '''
# 这是注释
# 这是注释
# 这是注释
# '''
# """
# 这是注释
# 这是注释
# 这是注释
# 三单引号注释和三双引号注释，第一个必须顶格
# """
# # 这是注释  单行注释（当行注释）


# ### 8.简述你所知道的Python3和Python2的区别？
# python3 print('something')
# python2 print 'something'
# ****
# python2 源码不统一，代码重复；输入，raw_input输出是什么类型，就是什么类型，可以是int、float、str；不支持中文 有整型和长整型（long int）之分
# python3 源码统一，代码不重复；输入input()都是字符串类型；支持中文   只有整型  没有长整型


# ### 9.提⽰⽤户输入大黑哥. 判断⽤户输入的对不对. 如果对, 提⽰真聪明, 如果不对, 提⽰输入有误
# name = input("请输入大黑哥:")
# if name == '大黑哥':
#     print('真聪明')
# else:
#     print('输入有误')


# ### 10.⽤户输⼊⼀个⽉份. 然后判断⽉份是多少⽉. 根据不同的⽉份, 打印出不同的饮⻝(根据个⼈习惯和⽼家习惯随意编写)
# month = int(input("请输入今天的月份:"))
# a = ['一月大口吃酒喝肉', '二月馒头拌咸菜', '三月吃土', '四月来工资了，大口吃酒，大口喝肉', '五月吃粽子', '六月吃饭',
#      '七月吃饭', '八月吃月饼', '九月吃饭', '吃十月的饭', '吃十一月的水饺', '吃十二月的鸡腿']
# if 0 < month <= 12:
#     print(a[month-1])
# else:
#     print("输入有误")

# ### 11.⽤户输⼊⼀个分数. 根据分数来判断⽤户考试成绩的档次
# print('*' * 40)
# print((' ' * 8) + "欢迎进入装*系统")
# print('*' * 40)
# score = int(input("请输入你考试的分数:"))
# if score < 60:
#     print('不及格')
# elif score < 70:
#     print('及格')
# elif score < 90:
#     print('良好')
# else:
#     print('优秀')
