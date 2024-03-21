# set of functions isalso called as function.

'''
user defined funtions

1.no return without argument
2.no return with argument
3.return without argument
4.return with argument

inbuild functions.....

upper()
Lower()

'''


n= int(input(" please choose the choice: "))

def first():
    
    print("first floor")
def second():
    
    print("second floor")

def Third():
    
    print("Third floor")

if(n==1):
    first()
if(n==2):
    second()
if(n==3):
    Third()

    
#1.no return without argument


def add():

    a= int(input("please enter the value A:"))

    b= int(input("please enter the value B:"))

    c= a+b
    print("Result:",c)
add()




#2.no return with argument


def sub(x,y):
    
    c= x-y
    print("Result:",c)

a= int(input("please enter the value A:"))

b= int(input("please enter the value B:"))

    
sub(a,b)



#3.return without argument

def mul():

    a= int(input("please enter the value A:"))

    b= int(input("please enter the value B:"))

    c= a*b

    return c
    
    
r=mul()
print("Result:",r)



#4. return with argument


def div(x,y):
    
    c= x/y
    return c
    

a= int(input("please enter the value A:"))

b= int(input("please enter the value B:"))

    
s=div(a,b)

print("Result:",s)
