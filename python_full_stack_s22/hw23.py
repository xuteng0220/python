
# 1.简答题：

# 面向对象的三大特性是什么？
# 继承 封装 多态

# 什么是面向对象的新式类？什么是经典类？
# 经典类是基类没有根(不继承其他的类)  新式类的基类都以object为父类
# py3都是新式类
# py2中，继承了object的是新式类，没有的是经典类。新式类的继承关系遵循mrc算法，经典类的继承关系遵循深度优先

# 面向对象为什么要有继承？继承的好处是什么？
# 子类能获得父类的属性和方法，减少代码的重复

# 好处:
# 增加了类的耦合性
# 减少了重复代码
# 是代码更加规范化,合理化
# 面向对象中super的作用。
# 可以在子类中重构父类的方法

##################################################################?????????????
# 2.代码题(通过具体代码完成下列要求)：

# class A:
#     def func(self):
#         print('in A')
#
# class B:
#     def func(self):
#         print('in B')
#
# class C(A,B):
#     def func(self):
#         print('in C')
# c1 = C()
# c1.func()
# 可以改动上面代码，完成下列需求：对C类实例化一个对象产生一个c1，然后c1.func()
# # 1. 让其执行C类中的func
# class A:
#     def func(self):
#         print('in A')

# class B:
#     def func(self):
#         print('in B')

# class C(A,B):
#     def func(self):
#         print('in C')

# c1 = C()
# c1.func()

************************************************************************************************
# 2. 让其执行A类中的func
class A:
    def func(self):
        print('in A')

class B:
    def func(self):
        print('in B')

class C(A,B):
	def func(self):
		super(C, self).func()

c1 = C()
c1.func()



# # 3. 让其执行B类中的func
class A:
    def func(self):
        print('in A')

class B:
    def func(self):
        print('in B')

class C(A,B):
	def func(self):
		super(A, self).func()

c1 = C()
c1.func()




# 4. 让其既执行C类中的func，又执行A类中的func
class A:
    def func(self):
        print('in A')

class B:
    def func(self):
        print('in B')

class C(A,B):
	def func(self):
		print('in C')
		super().func()

c1 = C()
c1.func()


# 5. 让让其既执行C类中的func，又执行B类中的func
class A:
    def func(self):
        print('in A')

class B:
    def func(self):
        print('in B')

class C(A,B):
	def func(self):
		print('in C')
		super(A, self).func()

c1 = C()
c1.func()

# # 3.下面代码执行结果是什么？为什么？
# class Parent(object):
#     def func(self):
#         print('in parent func')
#
#     def __init__(self):
#         self.func()
#
#
# class Son(Parent):
#     def func(self):
#         print('in son func')
#
# son1 = Son()
#
# # in son func 调用方法时，总是从自己的类空间中先找相应的方法或属性


# class A:
#     name = []
#
# p1 = A()
# p2 = A()
# p1.name.append(1)
# # p1.name，p2.name，A.name 分别是什么？[1][1][1]  name是类属性
# print(p1.name, p2.name, A.name)
#
# p1.age = 12
# print(p1.age)
# print(p2.age)
# print(A.age)
# # p1.age，p2.age，A.age 分别又是什么？为什么？18  报错  报错  age是实例属性


# # 4.写出下列代码执行结果：
# class Base1:
#     def f1(self):
#         print('base1.f1')
#
#     def f2(self):
#         print('base1.f2')
#
#     def f3(self):
#         print('base1.f3')
#         self.f1()
#
#
# class Base2:
#     def f1(self):
#         print('base2.f1')
#
#
# class Foo(Base1, Base2):
#     def f0(self):
#         print('foo.f0')
#         self.f3()
#
#
# obj = Foo()
# obj.f0()
#
# # foo.f0
# # base1.f3
# # base1.f1

# # 5.看代码写结果：
# class Parent:
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x,Child1.x,Child2.x) #1  1 1
#
# Child2.x = 2
# print(Parent.x,Child1.x,Child2.x) #1 1 2
#
# Child1.x = 3
# print(Parent.x,Child1.x,Child2.x)#1 3 2

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A):
#     pass
#
# class E(B,C):
#     pass
#
# class F(C,D):
#     pass
#
# class G(D):
#     pass
#
# class H(E,F):
#     pass
#
# class I(F,G):
#     pass
#
# class K(H,I):
#     pass
#
# print(K.__mro__)
写出mro算法的过程，见https://gitee.com/laonanhaipythonquanzhan24qi/19052823040/blob/master/day22/day22%E4%BD%9C%E4%B8%9A.md
