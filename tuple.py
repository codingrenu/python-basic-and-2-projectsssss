'''
tuple is one of the type of data type

it can allow duplicates.

it can used in rounded brackets.

functions 
count()
index()

list functions all are slightly matched in tuple but list can indicate square 
brackets.

and the same time tuple can indicate rounde brackets

'''


print("tuple")

a=(10,20,30,"ram",2.30,2,20,10+77j)

print("TUPLE:",a)


print("\n")

a=(10,20,30,"ram",2.30,2,20,10+77j)

c= a.count(20)

print("COUNT:",c)


print("\n")

b=(10,20,30,"ram",2.30,2,20,10+7j)

c=b.index(5)

print("INDEX:",c)



# number positive or negative 


s= int(input("please enter the number:,0"))


if(s<0):
    print("number ,s, is negative")

elif(a==0):
    print("number ,s, is neutral")

elif(s>0):
    print("number ,s, is positive")