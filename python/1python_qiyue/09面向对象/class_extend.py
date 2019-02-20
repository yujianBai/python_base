#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: class_extend.py
@time: 2019/2/19 15:54
"""

class Human():
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)

        '''
        代码开闭源自， 不能因为需改了付类方法，
        导致子类每部实现也需要修改
        super ,这里就体现了这个理论的应用
        
        '''
        # Human.__init__(self, name, age)

    def get_cout(self):
        return self.count


stu1 = Student("高新一中","石敢当",  18)
print (stu1.name, stu1.age, stu1.count, stu1.school)