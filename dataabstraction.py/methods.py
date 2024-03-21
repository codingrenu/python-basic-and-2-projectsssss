# types of methods

'''
1.instance methods


'''

#1.instance methods


class subject:

    method = "This is class method"

    def __init__(self,tamil,english,maths,science,socialscience):

        self.tamil=tamil
        self.english=english
        self.maths=maths
        self.science=science
        self.socialscience =socialscience

    def marks(self):# instance method

        total =self.tamil+self.english+self.maths+self.science+self.socialscience

        return total

    @classmethod
    
    def classmethod(cls): # class method is used to @classmethod decrator using
        
        return cls.method

    @staticmethod

    def staticmethod(): # static method is doesnt call in the parameter

        method = "This is static method"
        
        return method

    



obj=subject(95,98,90,99,100)

result =obj.marks()

print("RESULT:",result)

print(subject.classmethod()) # finally calling the classmethod function.

print(obj.staticmethod())



'''
output

RESULT: 482
This is class method
This is static method

'''

