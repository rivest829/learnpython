# -*- coding:utf-8 -*-
# Author Hsinhan Chiang

class School(object):
    def __init__(self,name):
        self.name=name
        self.registered_student=[]
    def create_lesson(self,name,price,cycle):
        l=Lesson(name,price,cycle)
        l.print_lesson()
        return l
    def create_group(self,name,lesson,teacher):
        g=Group(name,lesson,teacher)
        g.print_group()
        return g
    def create_teacher(self,name):
        t=Teacher(name,self)
        t.print_teacher()
        return t

class Lesson(object):
    def __init__(self,name,price,cycle):
        self.name=name
        self.price=price
        self.cycle=cycle
    def print_lesson(self):
        print('''
        -----------lesson-----------
        name=%s
        price=%s
        cycle=%s
        '''%(self.name,self.price,self.cycle))

class Student(object):
    def __init__(self,name,school,group):
        self.name=name
        self.school=school
        self.group=group
    def register(self):
        self.school.registered_student.append(self)
        for i in self.school.registered_student:
            print('register successful,%s'%(i.name))
    def pay(self):
        self.group.print_group()
        self.group.pay(self)

class Teacher(object):
    def __init__(self,name,school):
        self.name=name
        self.school=school
    def choose_group(self,group):
        self.group=group
    def show_group_student(self):
        for i in self.group.payed_student:
            print(i.name)
    def print_teacher(self):
        print('''
        ---------teacher----------
        name=%s
        school=%s
        ''' %(self.name,self.school.name))

class Group(object):
    name='classmethod'
    food='classhit'
    def __init__(self,name,lesson,teacher):
        self.name=name
        self.lesson=lesson
        self.teacher=teacher
        self.student = []
        self.payed_student = []
#静态方法：和类没什么关系，不能访问实例,不能访问类
    @staticmethod
    def eat1(name,food):
        print('%s is eating %s'%(name,food))
#类方法：和类有一丁点儿关系，只能访问类变量，不能访问实例
    @classmethod
    def eat2(self):
        print('%s is eating %s'%(self.name,self.food))
#属性方法:调用时可以像使用变量一样
    @property
    def eat3(self):
        print('%s is eating %s' % (self.name, self.food))
    @eat3.setter
    def eat3(self,name):
        self.name=name
        print('Now the name is %s'% name)

    @eat3.getter
    def eat3(self, name):
        self.name = name
        print('Now the name is %s' % name)
    def print_group(self):
        print('''
        ---------group----------
        name=%s
        lesson=%s
        teacher=%s
        ''' %(self.name,self.lesson.name,self.teacher.name))
    def pay(self,student):
        pay_money=input('You need to pay %s yuan:'%self.lesson.price)
        if int(pay_money)==int(self.lesson.price):
            self.payed_student.append(student)
            print('Pay Successful!')
        else:
            print('Pay Failed')
# peking=School('Peking')
# shanghai=School('Shanghai')
# linux=peking.create_lesson('linux',10000,'10weeks')
# teacher_liuc=peking.create_teacher('liu')
# group2017=peking.create_group('group2017',linux,teacher_liu)
# chiang=Student('Chiang',shanghai,group2017)
# chiang.register()
# chiang.pay()
a=Group(1,2,3)
a.eat3
a.eat3='nonnn'
a.eat3
del a.name
a.eat3