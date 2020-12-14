# # 1.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
#
# class Foo(object):
#     a1 = 1
#
#     def __init__(self,num):
#         self.num = num
#
#     def show_data(self):
#         print(self.num+self.a1)
#
#
# obj1 = Foo(666)
# obj2 = Foo(999)
# print(obj1.num)#666
# print(obj1.a1)#1
#
# obj1.num = 18
# obj1.a1 = 99
#
# print(obj1.num) #18
# print(obj1.a1)#99
#
# print(obj2.a1)#1
# print(obj2.num)#999
# print(obj2.num)#999
# print(Foo.a1) #1
# print(obj1.a1) #99


#########################################################################
# 测试实例对象修改类属性
# class Test(object):
#     dict_a = {1: "leo"}
#     num = 100
#
#     def __init__(self):
#         pass
#
#
# t1 = Test()
# print("--------Before--------")
# print(f't1.dict_a: {t1.dict_a}')
# print(f't1.num: {t1.num}')
# print(f'Test.dict_a: {Test.dict_a}')
# print(f'Test.num: {Test.num}')
# # 若类属性是可变对象，通过实例修改该属性，类属性也会被修改；不可变对象则无法通过实例修改
# t1.dict_a[2] = "mike"
# t1.num += 100
# print("--------After-------")
# print(f't1.dict_a: {t1.dict_a}')
# print(f't1.num: {t1.num}')
# print(f'Test.dict_a: {Test.dict_a}')
# print(f'Test.num: {Test.num}')
#########################################################################
# # 2.看代码写结果，注意返回值。
#
# class Foo(object):
#
#     def f1(self):
#         return 999
#
#     def f2(self):
#         v = self.f1()
#         print('f2')
#         return v
#
#     def f3(self):
#         print('f3')
#         return self.f2()
#
#     def run(self):
#         result = self.f3()
#         print(result)
#
#
# obj = Foo()
# v1 = obj.run()
# print(v1)
#
# # f3
# # f2
# # 999
# # None



# # 3.看代码写结果
# class Foo(object):
#     def __init__(self, num):
#         self.num = num
#
# v1 = [Foo for i in range(10)]
# v2 = [Foo(5) for i in range(10)]
# v3 = [Foo(i) for i in range(10)]
#
# print(v1)  # 10个类地址
# print(v2)  # 10个对象地址
# print(v3)  # 10个对象地址
#
# print(v1[1])


# # 4.看代码写结果
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     print(item.num)



# # 5.看代码写结果：
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     item.changelist(666)


# # 6.看代码写结果：
# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p3 = Person('安安', 19, d2)
#
# print(p1.name)
# print(p2.age)
# print(p3.depart)
# print(p3.depart.title)


# # 7.看代码写结果：
# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p1.message()
# p2.message()


# ####################################################################################################### ???
# # 看代码写结果：
# class A:
#     def f1(self):
#         print('in A f1')
#
# class B(A):
#     def f1(self):
#         print('in B f1')
#
# class C(A):
#     def f1(self):
#         print('in C f1')
#
# class D(B, C):
#     def f1(self):
#         super(B, self).f1()
#         super(C, self).f1()
#         print('in D f1')
#
# obj = D()
# obj.f1()
#
#
# # 9.看代码写结果：
# class A:
#     def f1(self):
#         print('in A f1')
#
# class B(A):
#     def f1(self):
#         super().f1()
#         print('in B f1')
#
# class C(A):
#     def f1(self):
#         print('in C f1')
#
# class D(B, C):
#     def f1(self):
#         super().f1()
#         print('in D f1')
#
# obj = D()
# print(D.__mro__)
# obj.f1()
# ##################################################################################################### ???



# 10.程序设计题：
# 运用类完成一个扑克牌类(无大小王)
# 的小游戏：
# 用户需要输入用户名，以下为用户可选选项:
# 1.
# 洗牌
# 2.
# 随机抽取一张
# 3.
# 指定抽取一张
# 4.
# 从小到大排序
# 5.
# 退出
#
# 1.
# 洗牌：每次执行的结果顺序随机。
# 2.
# 随机抽取一张：显示结果为：太白金星您随机抽取的牌为：黑桃K
# 3.
# 指定抽取一张：
# 用户输入序号（1
# ~52）
# 比如输入5，显示结果为：太白金星您抽取的第5张牌为：黑桃A
# 4.
# 将此牌从小到大显示出来。A -> 2 -> 3.......-> K
#
# 提供思路：
# 52
# 张牌可以放置一个容器中。
# 用户名，以及盛放牌的容器可以封装到对象属性中。
import random

class Poker:
    card = [i + j for i in ['Spade', 'Heart', 'Diamond', 'Club'] for j in [str(i) for i in range(2, 10)] + list('JQKA')]

    def __init__(self, name):
        self.name = name

    def shuffle_card(self):
        random.shuffle(self.card)
        print(self.card)


    def random_select(self):
        print(f"{self.name}您随机抽取的牌为：{random.sample(self.card, 1)[0]}")


    def specific_select(self):
        while True:
            num = int(input('请输入序号(1~52):'))
            if 0 < num < 53:
                print(self.card[num-1])
                break
            else:
                print(f"{num}超出范围了")

    def order_card(self):
        self.card.sort()  # 按首字母排序
        order_list = ['A'] + [str(i) for i in range(2, 10)] + list('JQK')
        order_dic = dict(zip(order_list, range(len(order_list))))
        self.card.sort(key = lambda x: order_dic[x[-1]])  # 按尾字母从A, 2, ..., K排序
        print(self.card)

    def quit(self):
        print('退出游戏')
        super().__del__()


p = Poker('ryan')
# print(p.card)
p.shuffle_card()
p.random_select()
p.specific_select()
p.order_card()
p.quit()
print(p.card)


# 方法一
import random
import copy
show = """
    1. 洗牌
    2. 随机抽取一张
    3. 指定抽取一张
    4. 从小到大排序
    5. 退出
"""
class Human:
    def __init__(self, name):
        self.name = name
    def randint(self,obj,n):
        print(f"{self.name}您随机抽取的牌为：{card[r]}")
    def choose(self,m,card):
        print(f"{self.name}您抽取的第{m+1}张牌为：{card[m]}")
    def shuffle(self, obj):
        random.shuffle(obj.poker(num, color))
num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
color = ["黑桃", "红桃", "梅花", "方片"]
class Poker:
    def __init__(self, num, color):
        self.num = num
        self.color = color
        self.poker_list = []
        self.card_list = []
    def poker(self, num, color):
        for i in num:
            for x in color:
                a = x + i
                self.poker_list.append(a)
        return self.poker_list
    def shuffle(self,obj):
        random.shuffle(obj)
    def take(self,obj):
        self.card_list.append(obj)
    def sort(self):
        p=Poker(num,color)
        print(poke.poker(num, color))
poke = Poker(num, color)
card = poke.poker(num, color)
# print(poke.poker(num, color))
l=[]
user = input("请输入您的用户名:").strip()
while 1:
    people=Human(user)
    print(show)
    n = input("请输入您的选择:").strip()
    if n.isdecimal() and 1 <= int(n)<=5:
        n=int(n)
        if n==1:
            poke.shuffle(card)
            # print(card)
        elif n==2:
            r=random.randint(0,51)
            people.randint(card,r)
            poke.take(card[r])
        elif n==3:
            m = input("请输入您选择牌的数字:").strip()
            if m.isdecimal() and 1 <= int(m) <= 52:
                m=int(m)-1
                people.choose(m,card)
                poke.take(card[m])
            else:
                print("您的输入有误,请您重新输入:")
                continue
        elif n==4:
            poke.sort()
        elif n==5:
            break
    else:
        print("您的输入有误,请您重新输入:")
        continue


# 法二:
import random

class Poker:

    num_list = ['A'] +[i for i in range(2,11)] + list('JQK')
    color_list = '黑桃 红桃 方片 梅花'.split()

    def __init__(self,name):
        self.name = name
        self.card = [(color, num) for color in self.color_list for num in self.num_list]


    def shuffle(self):
        random.shuffle(self.card)
        return self.card

    def _random(self):
        random_card = random.choice(self.card)
        return  f'{self.name} 您随机抽取的牌为：{random_card[0]}{random_card[1]}'

    def appoint(self):
        appoint_num = int(input('抽取第几张?(1~52)'))
        return f'{self.name} 您抽取的第{appoint_num}张牌为：{self.card[appoint_num-1][0]}{self.card[appoint_num-1][1]}'

    def sort(self):
        self.card = [(color, num) for num in self.num_list for color in self.color_list]
        return [(color, num) for num in self.num_list for color in self. color_list]

    def exit(self):
        exit()


choice_dict = {
    1: Poker.shuffle,
    2: Poker._random,
    3: Poker.appoint,
    4: Poker.sort,
    5: Poker.exit,

}

while 1:
    name = input('请输入用户名').strip()
    obj = Poker(name)
    while 1:
        choice_num = input('''
        1. 洗牌
        2. 随机抽取一张
        3. 指定抽取一张
        4. 从小到大排序
        5. 退出
        ''').strip()
        try:
            print(choice_dict[int(choice_num)](obj))
        except Exception :
            print('输入有误')

