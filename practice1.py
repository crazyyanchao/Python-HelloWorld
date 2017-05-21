#!/usr/bin/env python

#-------------------python基础笔记-----------------------
# 在不同环境中都可以运行加env
# 文件可执行命令chmod +x practice1.py
# print('hello world!')

# ipython notebook
# 上述命令打开了web端ipython
# python中变量不需要声明，直接用；不能用数字开头

# 字符编码：
# 1.ASCII[1byte] 只能127个字符
# 2.Unicode[2 bytes] 英文补够空出的一个byte
# 3.UTF-8[可变长编码] 对汉字三到六个bytes，比较节省空间
# UTF-8和Unicode一般转来转去的

# ord('A')查看字符编码；chr(66)查看编码的对应字符。
# sum = 0
# for i in range(100):
#     sum += i +1
# print(sum)

# sum1 = 0
# for i in range(100):
#     sum1 += sum1+1
#     if i == 2:
#         break
# print(sum1)

#!/usr/bin/env python  # chomd +x error.py
# try:
#     r = 10/0
# except ZeroDivisionError:
#     print('got it!')
# print('-------the end--------')
# 捕获异常不会让程序中断

# 将序列反序输出
# list = [1,2,3,4,5,6]
# # list.reverse()
# print(list)
# try:
#     for x in list:
#         print('\t',x)
# finally:
#     list.reverse()
#     print(list)

# sequence = [1,2,3,4,5,6]
# for i in range(len(sequence)-1,-1,-1):
#     x = sequence[i]
#     print(x)

# import  random
# print(random.random())
# print(random.randint(1,11))
# print(random.choice(range(11)))

# 参数传递：
# 1.位置传递
# def f(a,b,c):
#     return a+b+b
# print (f(1,2,3))

# 2.关键字传递
# print (f(a=1,b=2,c=3))

# 3.参数默认值
# def f1(a,b,c=10):
#     return a+b+c
# print(f1(1,2,3)) # 指定新的值不使用默认值

# 4.包裹传递 VS 解包裹
#--------------包裹传递----------------
# def func(*name):  # 包裹传递
#     print(type(name)) # 打印参数类型
#     print(name)
# print(func(1,2,3,4))  # 元组

# def func1(**name):
#     print(type(name))
#     print(name)
# print(func1(a=1,b=2,c=3)) # 字典      包裹关键字

#---------------解包裹--------------------
# def func3(a,b,c):
#     print(a,b,c)
# a=(1,2,3) # 元组
# print(func3(*a))
# b = {'a':1,'b':2,'c':3}
# print(func3(**b))
# 调用函数原则：先位置、后关键字、包裹位置、包裹关键字

# func = lambda a,b:a+b # 返回函数对象
# # print(func(1,2))
# def sum(f,x,y):
#     print('------in sum function-------')
#     return f(x,y)
# print(sum(func,2,8))  # 函数作为参数传递。函数即对象

# 类由变量和函数组成。类里面包含变量和方法，这种包含也称之为“封装”
# myClass = MyClass() 创建一个类的实例

# _init_()类似java中的构造函数
#-----------通过self调用类属性-------------
# class Human(object):
#     laugh = 'hahahaha'
#     def show_laugh(self):
#         print(self.laugh)
#     def laugh_10th(self):
#         for i in range(10):
#             self.show_laugh()
# xiaoming = Human()
# xiaoming.laugh_10th()
#-----------通过self增加类属性-------------
# class Human(object):
#     laugh = 'hahahaha'
#     def __init__(self,name):
#         self.name = name
#         print('_init_ is called')
#
#     def show_name(self):
#         print('My name is:'+self.name)
#
#     def show_laugh(self):
#         print(self.laugh)
#
#     def laugh_10th(self):
#         for i in range(10):
#             self.show_laugh()
# xiaoming = Human('xiaoming')
# xiaoming.show_name()
# xiaoming.show_laugh()
# 类的属性是对数据的封装，方法则是对类的行为的封装
#--------------属性和方法---------------
# 公有属性
# 内置属性，由系统定义类的时候默认添加，由前后两个下划线构成_dict_，_module_
# 私有属性：定义时在属性名前加双下划线
# 静态方法：相当于“全局函数”，其中无“self”语句
# 类方法：被classmethod（）函数处理过的函数
# 静态方法：相当与“全局函数”，其中无“self”语句
# self参数：指向对象本身

# 继承，python可以多继承。子类对父类属性和方法的共享
# class Bird(object):
#     have_feather = True
#     way_of_reproduction = 'egg'
#     def move(self,dx,dy):
#         position = [0,0]
#         position[0] = position[0] + dx
#         position[1] = position[1] + dy
#         return position
#
# # summer = Bird()
# # print('after move:',summer.move(5,8))
#
# class Chicken(Bird):
#     way_of_move = 'walk'
#     possible_in_KFC = True
# class Swan(Bird):
#     way_of_move = 'fly'
#     possible_in_KFC = False
#
# summer = Chicken()
# print(summer.have_feather)
# print(summer.move(5,8))

#-------------------模块---------------------
# 一个.py结尾的文件就是一个python模块
# 安装模块：pip install module_name
# 使用模块
# #!/usr/bin/env python
#
# '''
# this is a module example
# '''
#
# __author__ = 'YanchaoMa'
#
# import sys
#
# def test():
#     args = sys.argv # 局部变量  # 不加参数默认的是py文件的全名
#     print(args)
#     if len(args) == 1:
#         print('Hi,how are you ?')
#     elif len(args) == 2:
#         print('Hi,%s !'% args[1])  # 打印出第二个元素
#     else:
#         print('hahaha!')

# # 表达式为真，执行下面方法。下面代码在import的时候不会调用，是为了测试模块自身
# if __name__=='__main__':
#     test()

# 引入模块  import module_example  调用时：module_example.test()
# import m as k # 引入M并重命名为K
# from m import func1 # 从M中引入函数，直接使用
# from m import * # 从M中引入所有对象  # 调用模块中的对象  模块.对象
# 模块搜索路径
# （1）程序所在目录 （2)标准库的安装路径 (3)操作系统环境变量PYTHONPATH指向的路径
# 将自己的模块设置进去（长期使用）：export PYTHONPATH=$PYTHONPATH:<module_path>
# .pyc是字节码文件（由py文件执行之前被编译产生）（java和python都有编译的概念）

# 构建模块
# 模块包：同一文件夹下的功能相似的模块
# 声明模块包：__init__.py   （这个文件必须存在，可以是空的。标志着这是一个模块包）
# from 模块包 import x # 从模块包中引入模块x
# 删除某个字符结尾的文件 ：rm -f *c
# https://docs.python.org/3/library/index.html

# #!/usr/bin/env python
# import  re
# m = re.search('[0-9]','xxxxxxxxxxxx1xxxxxxxxxxxx')
# print(m.group(0))
# # 匹配0-9的数字，然后打印出匹配后的第一个元素

#---------------------python进阶---------------------
# python中一切皆对象
# 特殊方法：
# （1）以双下划线开头，并以双下划线结尾
# （2）__方法名__，例如：__init__
# （3）可以通过dir()查看对象所包含的特殊方法
#---------------------对象的属性----------------------
# #!/usr/bin/env python
# class Bird(object):
#     feather = True
#
# class Chicken(Bird):
#     fly = False
#     def __init__(self,age):
#         self.age = age
#
# chinck = Chicken(2)
#
# print(Bird.__dict__)
# print(Chicken.__dict__)    # python中对象的属性是由字典来管理的
# print(chinck.__dict__)
# # 通过字典这个属性系统，直接访问属性。也可以通过对象名字修改属性名。
# print('-----------------------------')
# chinck.__dict__['age'] = 3
# print(chinck.__dict__['age'])
# chinck.age = 10
# print(chinck.age)

#--------------设置相反数-------------
# #!/usr/bin/env python
# class num(object):
#     def __init__(self,value): # 特殊方法，对对象属性设置一个值
#         self.value = value
#     def getNeg(self):
#         return -self.value
#     def setNeg(self,value):
#         self.value = -value
#     def delNeg(self):
#         print('value also deleted')
#         del self.value
#     # （获得对象属性函数，设置对象属性参数，删除对象属性的接口，文档型秒速）
#     # 特性和对象属性有依赖关系
#     neg = property(getNeg,setNeg,delNeg,"I'm negative") # 特殊的属性
#
# x = num(1.1)
# print(x.neg)
# x.neg = -22
# print(x.value)
# print(num.neg.__doc__)
# del x.neg

# #!/usr/bin/env python
# class Bird(object):
#     feather = True
# class Chicken(Bird):
#     fly = False
#     def __init__(self,age):
#         self.age = age
#     def __getattr__(self, name):
#         if name == 'adult':
#             if self.age > 1.0:return True
#             else:return False
#         else:raise ArithmeticError(name)
#
# summer = Chicken(2)
# print(summer.adult) # 即时生成属性
# summer.age = 0.5 # 强行设置属性值。对象属性的值设置为0.5
# print(summer.adult)
#
# print(summer.male) # 即时生成属性
# ------设置特性的目的是当对象属性改变的时候，特性也会随之而改变---
# 查询即时生成的属性 __getattr_

# -------------------上下文管理器----------------------_
# 规定对象使用范围，超越范围则“采取处理”with...as...代码块
# 超越范围则用_exit__函数处理
# #!/usr/bin/env python
#
# # without context manager
# f = open("new.txt","w") # 写的方式打开
# print(f.closed) # 查看属性是否关闭，false表示没有关闭
# f.write("hello world!")
# f.close()
# print(f.closed)

# #!/usr/bin/env python
#
# # with context manager # 文件对象自动关闭，不用显示调用f.close()
#
# with open("new.txt","w") as f:
#     print(f.closed)
#     f.write("Hello World!......")
# print(f.closed)

# 任何定义了__enter__()和__exit__()方法的对象都可以用于上下文管理器
#!/usr/bin/env python

# class VOW(object):
#     def __init__(self,text):
#         self.text = text
#     def __enter__(self):
#         self.text = "enter:" + self.text # 添加前缀
#         return self  # 这里返回对象
#     def __exit__(self,exc_type,exc_value,traceback):
#         self.text = self.text + "now __exit__ !"  # 添加后缀
#
# with VOW("你好") as myvow:
#     print(myvow.text)
# print(myvow.text)

#---------------------闭包-----------------------
# 定义：一个包含有环境变量取值的函数对象。是一种组织代码的结构，
# 提高了代码的可重复使用性。
# #!/usr/bin/env python
#
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line  # 返回函数对象
#
# b = 5
# my_line = line_conf()
# print(my_line(5))

# #!/usr/bin/env python
#
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line  # 注意，返回函数对象
# b = 5
# my_line = line_conf()
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents) # 闭包的环境变量是第零号元素

# #!/usr/bin/env python
#
# def line_conf(a,b):
#     def line(x):
#         return a*x+b
#     return line
# line1 = line_conf(1,1)
# line2 = line_conf(4,5)
# print(line1(5),line2(5))

#---------------------装饰器-----------------------
# 可以包装函数，类的“函数”
# 包装函数的装饰器
# 【无参数代码示例】

# #!/usr/bin/env python
#
# # 计算平方和
# def square_sum(a,b):
#     print("input",a,b)
#     return a**2+b**2
#
# # 计算平方差
# def square_diff(a,b):
#     print("input",a,b)
#     return a**2-b**2
#
# print(square_sum(3,4))
# print(square_diff(3,4))

# #!/usr/bin/env python
#
# def deco(F):  # 接收一个可调用函数
#     def new_F(a,b):
#         print("input",a,b)
#         return F(a,b)
#     return new_F
#
# # 计算平方和
# @deco
# def square_sum(a,b):
#     return a**a+b**2
# # 计算平方差
# @deco
# def square_diff(a,b):
#     return a**2-b**2
# print(square_sum(3,4))
# print(square_diff(3,4))

# 【有参数代码示例】
# #!/usr/bin/env python
#
# # 新的包装层
# def pre_str(pre=''):
#     # 旧的装饰器
#     def decorator(F):
#         def new_F(a,b):
#             print(pre+"input",a,b)
#             return F(a,b)
#         return new_F
#     return decorator
#
# # 计算平方和
# @pre_str('hi +')
# def square_sum(a,b):
#     return a**2+b**2
# # 计算平方差
# @pre_str('hi -')
# def square_diff(a,b):
#     return a**2-b**2
#
# print(square_sum(3,4))
# print(square_diff(3,4))

# 包装类的装饰器
# #!/usr/bin/env python
#
# def decorator(aClass): # 接受一个类对象
#     class Newclass:
#         def __init__(self,age):
#             self.total_diaplay = 0
#             self.wrapped = aClass(age)
#         def display(self):
#             self.total_diaplay += 1
#             print("total display",self.total_diaplay)
#             self.wrapped.display()
#     return Newclass
# @decorator
# class Bird:
#     def __init__(self,age):
#         self.age = age
#     def display(self):
#         print("My age is",self.age)
# eagleLord = Bird(5)
#
# for i in range(3):
#     eagleLord.display()
# # 装饰器的目的就是进一步的包装函数，包装类

#-----------------------内存管理------------------------
# #!/usr/bin/env python
#
# # 引用计数
# from sys import getrefcount
#
# a = [1,2,3]
# print(getrefcount(a))
#
# b = [a,a]
# print(getrefcount(a))
#
# # #!/usr/bin/env python
#
# class from_obj(object):
#     def __init__(self,to_obj):
#         self.to_obj = to_obj
#
# b = [1,2,3]
# a = from_obj(b)
# print(id(a.to_obj))
# print(id(b))

# 循环对象：包含有一个next（）方法的对象。穷举结束后，抛出StopTteration错误
# f = open('new.txt')
# f.next()
# 用iter（）函数返回迭代对象

# 生成器：构成一个用户自定义的循环对象；yield关键字；
# #!/usr/bin/env python
#
# def gen():
#     a = 10
#     yield a
#     a = a*10
#     yield a
#     yield 1000
# for i in gen():
#     print(i)
# 生成器表达式，就是对上述代码的精炼表示。和表推导非常相似。
# G = (x**2 for x in range(3))
# G.next()

# 表推导。快速生成表的方法。
# l = [x**2 for x in range(3)]

# 动态类型：引用；引用与对象分离
# # 传值（值传递）
# a = 1
# def change_integer(a): # 值的拷贝
#     a = a + 1
#     pass # pass关键字表示占位，不执行具体操作
#     return a
# print(change_integer(a))
# print(a)
#
# # 传址（指针传递）
# b = [1,2,3]
# def change_list(b):   # 把地址中值修改了
#     b[0] = b[0] + 1
#     return b
# print(change_list(b))
# print(b)

#--------------------文件读写-------------------
# f = open(文件名，模式)  # r只读 w写入
# 读取、写入、关闭
# f.read(N)读N个byte，f.readline()读一行，f.readlines()读入多行
# f.write(str)   f.close()关闭

# OOP常见函数----面向对象编程常见函数
# #!/usr/bin/env python
#
# class Me(object):
#     def test(self):
#         print("hello!")
#
# def new_test():
#     print("New Hello!")
#
# me = Me()
#
# print(hasattr(me,"test"))           # 检查me对象是否有test属性
# print(getattr(me,"test"))           # 返回test属性
# print(setattr(me,"test",new_test))           # 将test属性设置为new_test
# print(delattr(me,"test"))           # 删除test属性
# print(isinstance(me,Me))            # me对象是否为Me类生成的对象
# print(issubclass(Me,object))        # Me类是否为object类的子类











