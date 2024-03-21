'''
collection of variablesand functions is also called as opps

oops can use the class and objects.
'''
'''
class oops:

    a=10

    def fun(self):
        print("this is oops concept")
  
obj=oops()
obj.fun()

print("the value of A:",obj.a)

'''

'''
class oops:
    
    def fun(self,name):
        print("Name:",name)
  
obj=oops()
obj.fun("Renu vijay")

'''

'''
class oops:
    
    def fun1(self,name,age):
        self.Name = name
        self.Age = age

    def fun2(self):
        print("Name:",self.Name)
        print("Age:",self.Age)
  
obj=oops()
obj.fun1("renu vijay",25)
obj.fun2()

'''


class Addition:

    def add(self):

        a= int(input("please enter the value A:"))
        b= int(input("please enter the value B:"))
        c=a+b
        print("Addition:",c)

    def mul(self):

        a= int(input("please enter the value A:"))
        b= int(input("please enter the value B:"))
        c=a*b
        print("Multiplication:",c)

class subtraction:

    def sub(self):

        a= int(input("please enter the value A:"))
        b= int(input("please enter the value B:"))
        c=a-b
        print("Subtraction:",c)


obj1=Addition()
obj1.add()
obj1.mul()

obj2=subtraction()
obj2.sub()






