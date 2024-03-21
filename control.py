'''
control statements in python

1. if(condition):
    statement

else:
    statement


2. if(condition):
    statement

elif(condition):
    statement

elif(condition):
    statement

else:
    statement

3.elif lader

4. nested if






'''

# 1. if 
a=10
b=20

if (a<b):
    print("B is bigger:",b)

else:
    print("A is bigger:",a)


# 2.if

a=20
b=10

if (a<b):
    print("B is bigger:",b)

else:
    print("A is bigger:",a)


# 3.if

a=20
b=10

if (a==b):
    print("A is equal to B")

else:
    print("A is not equal to B")



#  02. elif 


# number positive or negative 

'''
s= int(input("please enter the number:"))


if(s<0):
    print("number ,s, is negative")

elif(s==0):
    print("number ,s, is neutral")

elif(s>0):
    print("number ,s, is positive")

'''



# 03: given number is equal or not


num = int(input("please enter the number:"))



if(num==200):
    print("given ,num,is equal")


elif(num==200):
    print("given",num,"is equal")

elif(num==400):
    print("given",num,"is equal")

elif(num==500):
    print("given",num,"is equal")

else:
    print("given",num,"is not  equal")



# nested if


a= int(input("plese enter the number: "))

b= int(input("plese enter the number: "))



if(a!=b):
    print("a is not equal to b")

    if(a>b):
        print("A is greater than b")


    elif(a<b):
        print("B is greater than a")

    else:
        print("thank you")



else:
  print("a is equal to b")


