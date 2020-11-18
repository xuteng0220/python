# 1.面向对象的私有成员有什么？
# 私有类的静态属性
# 私有对象属性
# 私有类的方法

# 2.如何设置面向对象的类方法与静态方法，类方法静态方法有什么用？
# 类方法:@classmethod  得到可以实例化一对象,可以操作类的属性
# 静态方法:@staticmethod保持代码的一致性,提高代码的维护性


# 3.面向对象中属性是什么？有什么作用？
# @property   将动态方法伪装成属性,看起来更加合理


# 4.isinstance(a,b)判断a是否是b类的或b类派生类的对象
# issubclass(a,b)判断a类是否是b类或b类派生类的子类


# # 5.看代码写结果：
#
# class A:
#     a = 1
#     b = 2
#     def __init__(self):
#         self.c = 3
#         d = 4
#
# obj1 = A()
# obj2 = A()
# obj1.a = 3
# obj2.b = obj2.b + 3
# print(A.a) # 1
# print(obj1.b) # 2
# print(obj2.c) # 3
# print(obj2.b) # 5
# print(obj2.d) # 报错

# ####################################################????
# # 类的静态属性如果是可变对象，则当通过实例修改这个静态属性时，它会变化；如果是不可变对象，通过实例修改这个静态属性，相当于创建一个同名的类属性
# # # 6.看代码写结果：
# import os
# class Person:
#     name = 'aaa'
#
# p1 = Person()
# p2 = Person()
# p1.name += 'bbb'
# print(p1.name)  # bbb
# print(p2.name)  # aaa
# print(Person.name) # aaa
#
# # 7.看代码写结果：
# class Person:
#     name = []
#
# p1 = Person()
# p2 = Person()
# p1.name.append(1)
# p2.name.append(2)
# print(p1.name) # [1]
# print(p2.name)
# print(Person.name)


# # 看代码写结果：
# class A:
#     def __init__(self):
#         self.__func()
#     def __func(self):
#         print('in A __func')
#
# class B(A):
#     def __func(self):
#         print('in B __func')
#
# obj = B()  # in A __func  私有方法只能在类内部引用
#
#
# ################################################？？？？？
# # 9.看代码写结果：
# class Init(object):
#     def __init__(self, value):
#         self.val = value
#
# class Add2(Init):
#     def __init__(self, val):
#         super(Add2, self).__init__(val)
#         self.val += 2
#
# class Mul5(Init):
#     def __init__(self, val):
#         super(Mul5, self).__init__(val)
#         self.val *= 5
#
# class Pro(Mul5, Add2):
#     pass
#
# class Iner(Pro):
#     csup = super(Pro)
#     def __init__(self, val):
#         self.csup.__init__(val)
#         self.val += 1
#
# # 虽然没有见过这样的写法，其实本质是一样的，可以按照你的猜想来。
# p = Iner(5)
# print(p.val)


# 10.请按下列要求，完成一个商品类。

# 封装商品名，商品原价，以及折扣价。
# 实现一个获取商品实际价格的方法price。
# 接下来完成三个方法，利用属性组合完成下列需求：
#     利用属性property将此price方法伪装成属性。
#     利用setter装饰器装饰并实现修改商品原价。
#     利用deltter装饰器装饰并真正删除原价属性。




class Goods:

	def __init__(self):
		self.__origin_price = 100
		self.__discount = 0.8

	@property
	def price(self):
		actual_price = self.__origin_price * self.__discount
		return actual_price

	@price.setter
	def price(self, new_price):
		self.__origin_price = new_price

	@price.deleter
	def price(self):
		del self.__origin_price
	

apple = Goods()
print(apple.price)
apple.price = 1000
print(apple.price)
del apple.price
# print(apple.price)
