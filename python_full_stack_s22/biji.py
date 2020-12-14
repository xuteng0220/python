









##################################################################################


##############################################################
操作系统


I/O操作
    IO是相对于内存来说的

                Input       Output
    硬件        键盘         显示     
    文件操作     read        write
    网络操作     send        receive
    函数        input       print




计算机状态
    CPU工作
        做计算，对内存中的数据进行操作的时候CPU就是在工作
    CPU不工作
        IO操作的时候CPU不工作




不同的操作系统
    1.多道操作系统：一个程序遇到IO就把CPU让给其他程序，这样可以让多个程序连续使用CPU，使CPU不工作（等待）的时间尽量少，从而提高CPU的利用效率
    多道操作系统会在不同程序间切换，切换花的时间比连续使用CPU节省的时间少
    2.分时操作系统：把时间分成很小的段，每个时间都是时间片，每个程序轮流执行一个时间片——时间片的轮转。轮转没有提高CPU的利用率，但能提高了用户体验
    3.实时操作系统：
        比如，导弹制导所用的系统
    4.分布式操作系统


操作系统的作用
    统一分配计算机资源


进程： 在运行中的程序就是一个进程
    1.需要操作系统来调度它，会占用资源（内存、CPU等）
    2.pid：进程id，能够唯一标识一个进程，运行期间不会改变，重启一个进程会随机分配pid
    3.进程是计算机中最小的资源分配单位，一个进程起来，操作系统就会分配内存给它
    4.进程之间数据隔离，因为分配的内存块不同

并发：广义上：多个程序同时执行就是并发；狭义上，多个程序轮流在一个cpu上执行叫并发
    宏观上：多个程序是同时执行的
    微观上：多个程序轮流在一个cpu上执行，本质还是串行，只是轮流交替肉眼不可见
    
并行：
    多个程序同时执行，并且同时在多个cpu上执行


同步
    在做a的时候，发起了b时间，必须等待b结束之后才能继续做a
异步
    在做a的时候发起b，不需要等待b结束就可以继续a


阻塞/非阻塞
    如果cpu不工作，input accept recv recvfrom sleep connect/cpu在工作

线程
    线程存在于进程中，不能脱离进程存在
    线程是计算机中能够被cpu调度的最小单位


同步阻塞：判断是不是同步，有没有阻塞
    # py1.py
    def func(*arg):
        count = 0
        x = int(input("integer here"))
        for i in arg:
            count += 1
        return count

    a = 1
    b = 2
    c = a + b
    # 同步，func里需要input，会阻塞
    d = func(a, b, c)
    print(d)

同步非阻塞
    # py1.py
    def func(*arg):
        count = 0
        for i in arg:
            count += 1
        return count

    a = 1
    b = 2
    c = a + b
    d = func(a, b, c)
    # 同步，需要等待func执行完，才能执行print
    print(d)

异步阻塞
异步非阻塞
    举例：进程a运行的过程中，进程b启动（异步），进程a不受影响，继续运行（非阻塞）




进程的三状态图
    就绪：已准备好被cpu执行
    运行：cpu正在执行该进程
    阻塞：进程阻塞，cpu在等待
进程的调度算法
    给所有的进程分配资源或分配cpu使用权的一种方法
    a.有先来先服务，FCFS，哪个程序先到就先执行;
    b.短作业优先，哪个程序所用时间短就先执行短作业优先
    c.多级反馈算法
        有多人任务队列，优先级从高到低
        新来的任务总是优先级最高的
        每一个新任务机会会立即获得一个时间片的时间来执行（用户体验好，被重视）
        执行完一个时间片之后就会降到下一级队列中
        优先级高的队列中的任务都执行完以后才会执行优先级低的队列中的任务
        优先级越高时间片越短，反之越长，因为优先级高的都处理好了，优先级低的任务每个可以多执行一会


进程的开启和关闭
    开启，比如开机的时候运行的程序
    关闭，比如任务管理器中结束进程


开启子进程的方法，函数方式
from multiprocessing import Process
import os

def func():
    print(os.getpid(), os.getppid()) # getppid 父进程


if __name__ == '__main__': # 这一句在windows系统中需要，在mac/linux中不需要
    # 打印main进程及其父进程
    print('main: ', os.getpid(), os.getppid())
    # 将func函数作为目标传给类Process，实例化一个进程对象
    p = Process(target=func)
    # 开启这个进程对象，此时打印的是进程对象的pid及其父进程main的pid
    p.start()


向子进程传递参数
    def func(*args):
        pass
    
    # 通过属性args传递参数，且必须是一个tuple
    p = Process(target=func, args=(a, b, c))

父进程不能获取子进程的返回值
    因为父子进程的内存是隔离的，父到子，子进程开启的时候，有类似于copy（linux、mac）或import（windows）的机制，但子到父返回没有


开启多个子进程
from multiprocessing import Process
import os

def func(name, age):
    print(os.getpid(), os.getppid(), name, age) # getppid 父进程


if __name__ == '__main__': 
    print('main: ', os.getpid(), os.getppid())
    p = Process(target=func, args=('ryan', 30))
    p.start()
    p1 = Process(target=func, args=('isaac', 1))
    p1.start()




join的用法

import time
import random
from multiprocessing import Process

def send_email(name, age):
    print(f"给{age}岁的{name}发邮件")
    time.sleep(random.random())
    print('发送完毕')


if __name__ == '__main__':
    arg_lst = [('ryan', 30), ('isaac', 1), ('olivia', 28)]
    p_lst = []
    for arg in arg_lst:
        p = Process(target=send_email, args=arg)
        p.start() # start 异步非阻塞，调用一个函数，不需要等待这个函数的执行结果，并且在执行这个函数的过程中，CPU继续工作
        p_lst.append(p)
    for p in p_lst:
        p.join() # join 同步阻塞：直到p这个子进程执行完毕才继续执行主进程中的代码；若不阻塞，则异步非阻塞，会 导致主进程执行完毕，而子进程仍在执行，不符合发邮件的业务逻辑
    print('所有邮件都发送完毕')


多进程之间的数据是隔离的

from multiprocessing import Process
n = 0
def func():
    global n
    n += 1

print(n)
func()
print(n)

if __name__ = '__main__':
    p_lst = []
    for i in range(5):
        p = Process(target=func)
        p.start()
        p_lst.append(p)
    for i in p_lst:
        p.join()
    print(n)  # global只是进程中的全局变量，进程之间是隔离的，所以主进程的n不变




并发的socket进程

# server.py
import socket
from multiprocessing import Process

def talk(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
        reply = 'reply: ' + msg
        reply = reply.encode('utf-8')
        conn.send(reply)

if __name__ = '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        p = Process(target=talk, args=(conn,)).start()
    sk.close()


# client.py
import time
import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

while True:
    sk.send(b'hi')
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    # 看到消息来回的效果
    time.sleep(0.5)

sk.close()


P182 内容回顾



开启进程的另一种方式，使用面向对象的方法开启进程
import os
import time
from multiprocessing import Process

class MyProcess(Process):
    # override the run method in Process 
    def run(self):
        time.sleep(1) # 能看到并发的效果，但是为什么只会停留一秒，而不是循环的次数*1秒
        print(os.getppid(), os.getpid())



if __name__ == '__main__':
    print('主进程：', os.getpid())
    for i in range(8):
        p = MyProcess()
        p.start()




给子进程传递参数
class MyProcess(Process):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def run(self):
        print(os.getpid(), os.getppid(), self.a, self.b, self.c)

if __name__ == '__main__':
    print('主进程：', os.getpid())
    p = MyProcess(1, 2, 3)
    p.start()



守护进程
from multiprocessing import Process

def 


























############################################################
基础补遗


深浅拷贝

lst1 = [1, 2, 3]
lst2 = lst1
lst1.append('ryan')
print(lst2)

lst1存储了指向列表[1, 2, 3]的地址，赋值操作是把这个地址也存在了lst2中，当列表增加一个元素，lst1和lst2中的地址都不变

类比:一个人去吃饭，叫上了另一个人到同一张桌上，桌上的菜增加减少，对两个人来说都是相同的

def func(m):
    m[0] = 20
    m = [4, 5, 6]
    return m

l = [1, 2, 3]
func(l)
print('l = ', l)
print('func_result = ', func(l))



m = [1, 2, [3]]
n = m[:]
n[1] = 4
n[2][0] = 5
print(m) # [1, 2, [5]]




from copy import deepcopy
a = [3, 4]
m = [1, 2, a, [5, a]]
n = deepcopy(m)
n[3][1][0] = -1
print(n) # [1, 2, [-1, 4], [5, [-1, 4]]]


from copy import copy
from copy import deepcopy
m = [1, 2, [3, 4, 5], 6, [7, [8, 9]]]
n = m
n[0] = 7
n[2][0] = -1
print(n)
print(m)

m = [1, 2, [3, 4, 5], 6, [7, [8, 9]]]
n1 = copy(m)
n1[1] = -11
n1[2][1] = -7
print(n1)
print(m)

# 切片相当于浅copy
m = [1, 2, [3, 4, 5], 6, [7, [8, 9]]]
n2 = m[:]
n2[3] = -17
n2[2][2] = -5
print(n2)
print(m)

浅copy对不可变对象的子元素做修改或增删不会影响另一个对象
浅copy对可变对象的子元素做修改或增删会影响另一个对象
m = [1, 2, [3, 4, 5], 6, [7, [8, 9]], 10]
n3 = deepcopy(m)
n3[-1] = -10
n3[-2][0] = -7
print(n3)
print(m)









################################################################################
函数补遗


unpack，对于字典，unpack的是key
    a, b = {'name':'eva','age':18} 
    print(a)
    print(b)

dict中的value解包
    dic = {'name':'eva','age':18}
    name, age = dic.values()

    在函数中，可以通过**解包
    def func(a, b):
        print(a, b)

    func(**dic)



可变关键字参数
    def stu_info(**kwargs):
        print(kwargs)
        print(kwargs['name'],kwargs['sex'])
    # 传递时，key不用见引号
    stu_info(name = 'alex',sex = 'male')




命名空间的本质：存放名字与值的绑定关系

三种命名空间之间的加载与取值顺序：

加载顺序：
    内置命名空间(程序运行前加载)->
    全局命名空间(程序运行中：从上到下加载)->
    局部命名空间(程序运行中：调用时才加载)

取值顺序：
    在局部调用：局部命名空间->全局命名空间->内置命名空间
    在全局调用：全局命名空间->内置命名空间




nonlocal使用
    
    def f1():
        a = 1
        def f2():
            a = 2
        f2()
        print('a in f1 : ',a)

    f1() # a in f1 : 1


    def f1():
        a = 1
        # a 是一个不可变对象，在内层函数改变，需要用nonlocal。如果是可变对象，不用nonlocal也能改变
        def f2():
            nonlocal a
            a = 2
        f2()
        print('a in f1 : ',a)

    f1() # a in f1 : 2








闭包
https://www.cnblogs.com/Eva-J/articles/7156261.html





################################################################################
可迭代对象 迭代器  生成器 补遗

迭代器和可迭代对象方法的不同
    print(set(dir([1,2].__iter__()))-set(dir([1,2])))
    print(set(dir([1,2]))-set(dir([1,2].__iter__())))




类的三大装饰器
class Classmethod_Demo():
    role = 'dog'

    @classmethod
    def func(cls):
        print(cls.role)

    def __init__(self):
        pass

    def func1(self):
        print('in func1')

Classmethod_Demo.func()


demo1 = Classmethod_Demo()
demo1.func() # 实例调用类方法
demo1.func1() # 实例调用实例的绑定方法
Classmethod_Demo.func() # 类调用类方法
# Classmethod_Demo.func(demo1) # 报错
Classmethod_Demo.func1(demo1) # 实例调用实例方法
# Classmethod_Demo.func1()  # 报错






##################################################################################

类 补遗

egg = Person('egon')  #类名()就等于在执行Person.__init__()


如何让通过实例修改类的静态变量，且这个变量是不可变对象
class Person:
    hair_color = 'white'

    def __init__(self, name):
        self.name = name

p1 = Person('ryan')
p1.hair_color = 'red'
print(p1.hair_color)

p2 = Person('oli')
print(p2.hair_color)
p2.__class__.hair_color = 'black'  # 实例名.__class__获取该实例所属的类
print(p2.hair_color)

p3 = Person('isaac')
print(p3.hair_color)



# 类的静态属性如果是可变对象，则当通过实例修改这个静态属性时，它会变化；如果是不可变对象，通过实例修改这个静态属性，相当于创建一个同名的类属性
# # 6.看代码写结果：
import os
class Person:
    name = 'aaa'

p1 = Person()
p2 = Person()
p1.name += 'bbb'
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name) # aaa

# 7.看代码写结果：
class Person:
    name = []

p1 = Person()
p2 = Person()
p1.name.append(1)
p2.name.append(2)
print(p1.name) # [1]
print(p2.name)
print(Person.name)




如何获取类的内存地址？？？ 即显示object at 0x******
class Person:

    def __init__(self, name):
        self.name = name

    def func():
        pass

print(Person.func)
p = Person('ryan')
print(p.func)
print(Person.__dict__)