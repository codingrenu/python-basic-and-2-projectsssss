# inheritnce in python.

'''
inheritance is mainlyto used to memeory reduce purpose use

they are five types

1.single in heritance.....

        one base class
        one derived class

2.multiple in heritance.....

        one base class
        two derived class

3.multilevel in heritance.....

        two base class
        one derived class


4.herarichal in heritance.....

        one base class
        three derived class

5 hybrid heritance.....

       a- one base class
        b c-two derived class

        bc-d combine-one derived class




'''

#single inheritance:

class Addition:

    def add(self):

        a= int(input("please enter the value A:"))

        b= int(input("please enter the value B:"))

        c= a+b

        print("Addition:",c)

class  subtraction(Addition):

    def sub(self):

        a= int(input("please enter the value A:"))

        b= int(input("please enter the value B:"))

        c= a-b

        print("Subtraction:",c)


obj=subtraction()

obj.add()
obj.sub()



#multiple inheritance:

class Addition:

    def add(self):

        a= int(input("please enter the value A:"))

        b= int(input("please enter the value B:"))

        c= a+b

        print("Addition:",c)

class  subtraction:

    def sub(self):

        a= int(input("please enter the value A:"))

        b= int(input("please enter the value B:"))

        c= a-b

        print("Subtraction:",c)


class inputvalues(Addition,subtraction):

    def say(self):

      self.add()
      self.sub()


obj =inputvalues()
obj.say()


# hierarchicalinheritance

class Get:
    def getin(self):
        self.a = int(input("please enter the value A:"))
        self.b = int(input("please enter the value B:"))

class Addition(Get):
    def add(self):
        self.getin()
        c = self.a + self.b
        print("Addition:", c)

class Subtraction(Get):
    def sub(self):
        self.getin()
        c = self.a - self.b
        print("Subtraction:", c)

obj1 = Addition()
obj1.add()

obj2 = Subtraction()
obj2.sub()
  


# hybrid inheritance
class Get:
    def getin(self):
        self.a = int(input("please enter the value A:"))
        self.b = int(input("please enter the value B:"))

class Addition(Get):
    def add(self):
        self.getin()
        c = self.a + self.b
        print("Addition:", c)


class subtraction(Get):
    def sub(self):
        self.getin()
        c = self.a - self.b
        print("subtraction:", c)

class arithmetic(Addition,subtraction):
    def arith(self):
        self.add()
        self.sub()

obj=arithmetic()

obj.arith()

      








