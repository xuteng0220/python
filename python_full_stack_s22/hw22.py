# # # # 1.暴力摩托程序（完成下列需求）：
# # # #     1.创建三个游戏人物，分别是：
# # # # 	苍井井，女，18，攻击力ad为20，血量200
# # # # 	东尼木木，男，20，攻击力ad为30，血量150
# # # # 	波多多，女，19，攻击力ad为50，血量80
# # # #     2.创建三个游戏武器，分别是：
# # # #      平底锅，ad为20
# # # # 	斧子，ad为50
# # # # 	双节棍，ad为65
# # # #     3.创建三个游戏摩托车，分别是：
# # # # 小踏板，速度60迈
# # # # 雅马哈，速度80迈
# # # # 宝马，速度120迈。
# # # # 完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：
# # # # （1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
# # # # （2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
# # # # （3）波多多骑着雅马哈开着80迈的车行驶在赛道上。
# # # # （4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
# # # # （5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。
# # # # （6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
# # # # （7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
# # # # （8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。（选做）
# # # # (9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。（选做）
# # #
# # # class role:
# # #     def __init__(self, name, gender, age, ad, hp):
# # #         self.name = name
# # #         self.gender = gender
# # #         self.age = age
# # #         self.ad = ad
# # #         self.hp = hp
# # #
# # #     def ride(self, moto_obj):
# # #         print(f'{self.name}骑着{moto_obj.name}开着{moto_obj.speed}迈的车行驶在赛道上')
# # #
# # #     def attack(self, other_role, weapon_obj=None):
# # #         if weapon_obj is None:
# # #             other_role.hp -= self.ad
# # #             msg = f'{self.name}赤手空拳打了{other_role.name}{self.ad}滴血，{other_role.name}还剩{other_role.hp}血'
# # #         else:
# # #             other_role.hp = other_role.hp - self.ad - weapon_obj.ad
# # #             msg = f'{self.name}利用{weapon_obj.name}打了{other_role.name}一{weapon_obj.name}，{other_role.name}还剩{other_role.hp}血'
# # #         print(msg)
# # #
# # #     def ride_attack(self, other_role):
# # #         other_role.hp -= self.ad + self.weapon_obj.ad
# # #         msg = f'{self.name}骑着{self.moto_obj.name}打了骑着{other_role.moto_obj.name}的{other_role.name}一{self.weapon_obj.name}，{other_role.name}哭了，{other_role.name}还剩{other_role.hp}血'
# # #         print(msg)
# # #
# # # class weapon:
# # #     def __init__(self, name, ad):
# # #         self.name = name
# # #         self.ad = ad
# # #
# # #     # def attack(self):
# # #     #     pass
# # #
# # # class moto:
# # #     def __init__(self, name, speed):
# # #         self.name = name
# # #         self.speed = speed
# # #
# # #     # def ride(self, role_obj):
# # #     #     msg = f"{role_obj.name}骑着{self.name}开着{self.speed}迈的车行驶在赛道上"
# # #     #     print(msg)
# # #
# # # role_cang = role('苍井井', '女', 18, 20, 200)
# # # role_dong = role('东尼木木', '难', 20, 30, 150)
# # # role_bo = role('波多多', '女', 19, 50, 80)
# # #
# # # weapon_guo = weapon('平底锅', 20)
# # # weapon_fu = weapon('斧子', 20)
# # # weapon_gun = weapon('双截棍', 20)
# # #
# # # moto_taban = moto('小踏板', 60)
# # # moto_yamaha = moto('雅马哈', 80)
# # # moto_baoma = moto('宝马', 120)
# # #
# # # role_cang.ride(moto_taban)
# # # role_dong.ride(moto_baoma)
# # # role_bo.ride(moto_yamaha)
# # # role_cang.attack(role_bo)
# # # role_dong.attack(role_bo)
# # # role_bo.attack(role_cang, weapon_guo)
# # # role_bo.attack(role_dong, weapon_fu)
# # #
# # # role_cang.moto_obj = moto_baoma
# # # role_cang.weapon_obj = weapon_gun
# # # role_dong.moto_obj = moto_taban
# # #
# # # role_bo.moto_obj = moto_taban
# # # role_bo.weapon_obj = weapon_fu
# # # role_dong.moto_obj = moto_yamaha
# # #
# # # role_cang.ride_attack(role_dong)
# # # role_bo.ride_attack(role_dong)
# # #
# # #
# # #
# # #
# # # class Role:
# # #
# # #     def __init__(self,name,sex,age,ad,blood):
# # #         self.name = name
# # #         self.sex = sex
# # #         self.age = age
# # #         self.ad = ad
# # #         self.blood = blood
# # #
# # #     def fight(self, beaten):
# # #         beaten.blood -= self.ad
# # #         print(f"{self.name}赤手空拳大了{beaten.name}{self.ad}滴血,{beaten.name}还剩下{beaten.blood}")
# # #     def fight2(self,beaten):
# # #         beaten.blood -= self.ad + self.weapon.ad
# # #         print(f"{self.name}骑着{self.motorcycle.name}打了骑着{beaten.motorcycle.name}的{beaten.name}一{self.weapon.name},{beaten.name}哭了,还剩{beaten.blood}")
# # #
# # # class Weapon:
# # #
# # #     def __init__(self,name,ad):
# # #         self.name = name
# # #         self.ad = ad
# # #
# # #     def finght(self,p1,p2):
# # #         p2.blood -= p1.ad +self.ad
# # #         print(f"{p1.name}利用{self.name}打了{p2.name}一{self.name},{p2.name}还剩{p2.blood}血")
# # #
# # # class Motorcycle:
# # #
# # #     def __init__(self,name,speed):
# # #         self.name = name
# # #         self.speed = speed
# # #
# # #     def drving(self,who):
# # #         print(f"{who.name}骑着{self.name}开着{self.speed}迈的车行驶在赛道上.")
# # #
# # # cjj = Role("苍井井","女",18,20,200)
# # # dnmm = Role("东尼木木","男",20,30,150)
# # # bdd = Role("波多多","女",19,50,80)
# # #
# # # pdg = Weapon("平底锅",20)
# # # fz = Weapon("斧子",50)
# # # sjg = Weapon("双截棍",65)
# # #
# # # xtb = Motorcycle("小踏板",60)
# # # ymh = Motorcycle("雅马哈",80)
# # # bm = Motorcycle("宝马",120)
# # #
# # # cjj.motorcycle = xtb
# # # dnmm.motorcycle = bm
# # # bdd.motorcycle = ymh
# # #
# # # cjj.motorcycle.drving(cjj)
# # # dnmm.motorcycle.drving(dnmm)
# # # bdd.motorcycle.drving(bdd)
# # #
# # # cjj.fight(bdd)
# # # dnmm.fight(bdd)
# # #
# # # bdd.weapon = pdg
# # # bdd.weapon.finght(bdd,cjj)
# # # bdd.weapon = fz
# # # bdd.weapon.finght(bdd,dnmm)
# # #
# # # cjj.motorcycle = bm
# # # cjj.weapon = sjg
# # # dnmm.motorcycle = xtb
# # #
# # # cjj.fight2(dnmm)
# # # bdd.motorcycle = xtb
# # # bdd.weapon = fz
# # # dnmm.motorcycle =ymh
# # # bdd.fight2(dnmm)
# #
# #
# # # 2.定义一个类，计算圆的周长和面积。
# # from math import pi
# # class Circle:
# #     def __init__(self, r):
# #         self.r = r
# #
# #     def area(self):
# #         return pi * self.r ** 2
# #
# #     def peremiter(self):
# #         return pi * self.r * 2
# #
# # yuan1 = Circle(1)
# # print(yuan1.area())
# # print(yuan1.peremiter())
# #
# # # 3.定义一个圆环类，计算圆环的周长和面积（升级题）
# # class Ring(Circle):
# #     def __init__(self, inner_r, outer_r):
# #         self.inner_r, self.outer_r = (inner_r, outer_r) if inner_r < outer_r else (outer_r, inner_r)
# #         self.inner_circle = Circle(self.inner_r)
# #         self.outer_circle = Circle(self.outer_r)
# #
# #     def area(self):
# #         return self.outer_circle.area() - self.inner_circle.area()
# #
# #     def peremiter(self):
# #         return self.outer_circle.peremiter() + self.inner_circle.peremiter()
# #
# #
# # r34 = Ring(3, 4)
# # print(r34.area())
# # print(r34.peremiter())
# #
# # '''
# 定义一个学校类，一个老师类。
#
# 学校类要求：
#
# 学校类封装学校名称，学校地址，以及相关老师（以列表形式存放老师对象）的属性。
#
# name: 学校名称。
# address: 具体地址。
# teacher_list: []。
# 学校类设置添加老师对象的方法。
#
# 老师类封装姓名，教授学科，以及所属学校的具体对象。
#
# name: 老师名。
# course: 学科。
# school: 具体学校对象。
# 实例化2个校区：
#
# 北京校区，美丽的沙河；
# 深圳校区，南山区。
# 实例化6个老师：
#
# 太白，Python, 北京校区对象。
# 吴超，linux, 北京校区对象。
# 宝元，python, 北京校区对象。
# 苑昊，python, 深圳校区对象。
# 小虎，linux, 深圳校区对象。
# 小王，Python，深圳校区对象。
# 完成以下具体需求：
#
# 获取太白所属学校名称。
#
# 获取太白所属学校的学校地址。
#
# 将所有属于北京校区的所有老师名展示出来，并添加到一个列表中。
#
# 将所有属于深圳校区的所有老师以及所负责的学科展示出来。
#
# 将两个校区的负责Python学科的所有老师对象添加到一个列表中。
#
# 将两个校区的负责linux学科的所有老师对象添加到一个列表中并循环展示出来。
#
# 将北京校区这个对象利用pickle写入文件中，然后读取出来，并展示出所属于北京校区的老师姓名。
# '''

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teacher_list = []

    def add_teacher(self, new_teacher):
        self.teacher_list.append(new_teacher)
        return self.teacher_list

class Teacher:
    def __init__(self, name, course, school):
        self.name = name
        self.course = course
        self.school = school
        # 这句关键，要清楚self的意义，就是实例对象
        self.school.add_teacher(self)

bj_school = School('beijing_campus', 'shahe')
sz_school = School('shenzhen_campus', 'nanshan')


taibai = Teacher('taibai', 'python', bj_school)
wusir = Teacher('wusir', 'linux', bj_school)
baoyuan = Teacher('baoyuan', 'python', bj_school)
yuanhao = Teacher('yuanhao', 'python', sz_school)
xiaohu = Teacher('xiaohu', 'linux', sz_school)
xiaowang = Teacher('xiaowang', 'python', sz_school)

print(taibai.school.name)
print(taibai.school.address)


# # teacher类中 self.school.add_teacher(self)就可以完成下面的功能
# teachers = [taibai, wusir, baoyuan, yuanhao, xiaohu, xiaowang]
# for teacher in teachers:
#     if teacher.school.name == 'beijing_campus':
#         bj_school.add_teacher(teacher)
#     else:
#         sz_school.add_teacher(teacher)
bj_teacher = bj_school.teacher_list
bj_teacher_name = []
for teacher in bj_teacher:
    bj_teacher_name.append(teacher.name)
print(bj_teacher_name)

sz_teacher = sz_school.teacher_list
sz_teacher_dic = {}
for teacher in sz_teacher:
    sz_teacher_dic[teacher.name] = teacher.course
print(sz_teacher_dic)


python_teacher = list(filter(lambda x:x.course == 'python', bj_teacher + sz_teacher))
python_teacher_name = [i.name for i in python_teacher]
linux_teacher = list(filter(lambda x:x.course == 'linux', bj_teacher + sz_teacher))
linux_teacher_name = [i.name for i in linux_teacher]

# all_teacher = bj_teacher + sz_teacher
# python_teacher = []
# linux_teacher = []
# for teacher in all_teacher:
#     if teacher.course == 'python':
#         python_teacher.append(teacher.name)
#     else:
#         linux_teacher.append(teacher.name)
print(python_teacher_name)
print(linux_teacher_name)

# 将北京校区这个对象利用pickle写入文件中，然后读取出来，并展示出所属于北京校区的老师姓名。
import pickle
f = open('hw22_pickle', 'wb')
pickle.dump(bj_school, f)
f.close()
f = open('hw22_pickle', 'rb')
bj_school2 = pickle.load(f)
f.close()
bj_teacher_name2 = [i.name for i in bj_school2.teacher_list]
print(bj_teacher_name2)


