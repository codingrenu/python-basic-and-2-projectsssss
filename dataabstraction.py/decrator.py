# decorator in python..

'''

it doesn't to touch the behavoiual of the function but use the
another function to change the functions is called decrator .


'''


# decorator in python..

def outerfunction():
    msg1="welcome to"

    def innerfunction(): # nested function
        msg2="python"

        out =msg1+ msg2

        return out
    
    return innerfunction  # function return another function

obj = outerfunction()
print(obj()) # function as a reference.



'''
print(obj)<function outerfunction.<locals>.innerfunction at 0x000001D291F21080>

print(obj.__name__)    innerfunction

print(obj())   welcome to python


'''

# 2. function as a parameter.

def myfunction1():
    print("This is function-1")

def myfunction2(ref):
    print(ref())
    print("This is function-2")
    print(ref.__name__)
    
    print(ref)

myfunction2(myfunction1)


#3. single decrator

def upperstring(ref):
    def process():

        data=ref()

        return data.upper()
    
    return process
        

@upperstring

def function():
    return "welcome to renu"


print(function())

'''

the code alternate use the @upperstring

and function above initialise @upperstring and function beolw use the function calling


code...


@upperstring...this is single decrotor

def function():
    return "welcome to renu"


print(function())



print(function())

result =function()

result =upperstring(function)

print(result())
print(result)

print(result.__name__)



'''

'''
output:
welcome to renu
WELCOME TO RENU
<function upperstring.<locals>.process at 0x0000027A419F1580>
process

'''



#4. multiple decrator

def upperstring(ref):
    def process():

        data=ref()

        return data.upper()
    
    return process
        

def split(ref):
    def process():

        data=ref()

        return data.split()
    
    return process
        




@split
@upperstring

def function():
    return "welcome to renu"


print(function())



#5.decrator with parameter
'''
decrator with parameter is using two functionis necessary


'''




def outerfunction(str):

    def upperstring(ref):
        def process():
            data=ref()
            return data.upper() + str
        return process
    return upperstring


@outerfunction(" this is parmeter passing decarator ")

def function():

    return "welcome to python"


print(function())




# function decrator

def outerfunction(ref):
    
    def innerfunction(*args):

        return ref(*args).upper()
    
    return innerfunction


@outerfunction

def myfunction(str1,str2):

    return f' Hello  {str1} and  {str2} '

print(myfunction('Renu','Ram'))

'''
obj =outerfunction(myfunction)

print(obj('Renu','Ram'))

'''



#class decrator

class mydecrator:

    def __init__(self,ref):

        self.ref=ref

    def __call__(self,*args):

        return self.ref(*args).upper()
        

        



def myfunction(str1,str2):

    return f' Hello  {str1} and  {str2} '

obj = mydecrator(myfunction)

obj('gokul','hari')

    








#class decrator

class mydecrator:

    def __init__(self,ref):

        self.ref=ref

    def __call__(self,*args):

        return self.ref(*args).upper()
        

@mydecrator       
def myfunction(str1,str2):

    return f' Hello  {str1} and  {str2} '


print(myfunction("gokul","hari"))


'''
obj = mydecrator(myfunction)

print(obj("gokul","hari"))

    



class decrator is used in the call function default print(obj("gokul","hari")


'''
