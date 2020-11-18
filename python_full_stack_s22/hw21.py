############################################################
# 接口类和抽象类有什么区别


############################################################




# # 1.创建一个人类Person,再类中创建3个静态变量(静态字段)
# #     animal = '高级动物'
# #     soul = '有灵魂'
# #     language = '语言'
#
# class Person():
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
# ryan = Person()
# print(ryan.animal)
# print(ryan.soul)
# print(ryan.language)



# # 2.在类中定义三个方法,吃饭,睡觉,工作.
# class Person():
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def eat(self):
#         print('吃饭')
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
# ryan = Person()
# ryan.eat()
# ryan.sleep()
# ryan.work()


# # 3.在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄,  身高.
# class Person():
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, gender, age, height):
#         self.country = country
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.height = height
#
#     def eat(self):
#         print('吃饭')
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
# ryan = Person('china', 'ryan', 'male', 30, 170)
# ryan.name
# ryan.eat()


# # # 4.实例化四个人类对象:
# # #     第一个人类对象p1属性为:中国,alex,未知,42,175.
# # #     第二个人类对象p2属性为:美国,武大,男,35,160.
# # #     第三个人类对象p3属性为:你自己定义.
# # #     第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3  的身高.
# class Person():
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, gender, age, height):
#         self.country = country
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.height = height
#
#     def eat(self):
#         print('吃饭')
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# p2 = Person('美国', '武大', '男', 35, 160)
# p3 = Person('china', 'ryan', 'male', 30, 170)
# p4 = Person(p1.country, p2.name, p3.gender, p2.age, p3.height)
# print(p4.country)
# print(p4.age)


# # 5.通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
# # 6.通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
# # 7.通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
# class Person():
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, gender, age, height):
#         self.country = country
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.height = height
#
#     def eat(self):
#         print(f'{self.name}在吃饭')
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# p1.eat()
# p2 = Person('美国', '武大', '男', 35, 160)
# p2.eat()
# p3 = Person('china', 'ryan', 'male', 30, 170)
# p3.eat()


# # 8.通过p1对象找到Person的静态变量 animal
# class Person():
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, gender, age, height):
#         self.country = country
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.height = height
#
#     def eat(self):
#         print(f'{self.name}在吃饭')
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# print(p1.animal)


# # 2.通过自己创建类,实例化对象在终端输出如下信息
# # 小明，10岁，男，上山去砍柴
# # 小明，10岁，男，开车去东北
# # 小明，10岁，男，最爱大保健
# # 老李，90岁，男，上山去砍柴
# # 老李，90岁，男，开车去东北
# # 老李，90岁，男，最爱大保健
# # 老张…
#
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     # def hobby(self):
#     #     print(f'{self.name}，{self.age}岁，{self.gender}，上山去砍柴')
#     #     print(f'{self.name}，{self.age}岁，{self.gender}，开车去东北')
#     #     print(f'{self.name}，{self.age}岁，{self.gender}，最爱大保健')
#
#     def hobby(self, action):
#         print(f'{self.name}，{self.age}岁，{self.gender}，{action}')
#
# p1 = Person('小明', 10, '男')
# p2 = Person('老李', 90, '男')
# p1.hobby('开车去东北')



# # 3.设计一个汽车类。
# # 要求：
# # 汽车的公共属性为：动力驱动，具有四个或以上车轮，主要用途载运人员或货物。
# # 	汽车的功能：run,transfer.
# # 具体的汽车的不同属性：颜色，车牌，类型（越野，轿车，货车等）。
# class Car:
#     power = 'oli'
#     ties = 4
#     usage = '载人货运'
#
#     def __init__(self, color, plate, car_type):
#         self.color = color
#         self.plate = plate
#         self.car_type = car_type
#
#     def run(self):
#         print('car can run')
#
#     def transfer(self):
#         print('car can transfer')
#
# honda = Car('while', 'EMH217', 'SUV')
# print(honda.usage)
# print(honda.plate)
# honda.run()



# 3. 模拟英雄联盟写一个游戏人物的类（升级题）.
#    要求:
#    1. 创建一个 Game_role的类.
#    2. 构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#    3. 创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
#           例: 实例化一个对象 盖伦,ad为10, hp为100
#           实例化另个一个对象 剑豪 ad为20, hp为80
#           盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血,  还剩多少血'的提示功能.
class Game_role:

    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, other_player):
        other_player.hp -= self.ad
        print(f"{self.name}攻击了{other_player.name}， {other_player.name}掉了{self.ad}血，还剩{other_player.hp}血")

gailun = Game_role('盖伦', 10, 100)
jianhao = Game_role('剑豪', 20, 80)
gailun.attack(jianhao)









