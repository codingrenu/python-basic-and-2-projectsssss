# for loop in python.

n = int(input("\n please enter the limit"))

for i in range(1,n+1):
    print(i)





# tabl in for loop

t = int(input("\n please enter the table:"))

n= int(input("\n please enter the limit:"))


for i in range(1,n+1):

    print(i,"*",t,"=",i*t)



# odd number & even number:

n= int(input("please enter the limit:"))


print("\n odd number")
             
for i in range(n):
             if(i%2!=0):
                print(i)

print("\n even number")
             
for i in range(n):
             if(i%2==0):
                print(i)











#03.. sum of n numbers:

n=int(input("plese enter the limit:"))

sum = 0

for i in range(1,n+1):

    sum =sum+i

    print("sum of number is:",sum)


# 04sum of number isdivisible by 5.

n=int(input("plese enter the limit:"))


for i in range(1,n+1):

    if(i%5==0):
        print(i)

    

                
             


             
             
             
# reverse print the sum of numbers.


print("\n reverse print")


n=int(input("please enter the limit:"))


for i in range(n,0,-1):
    print(i)



# three multiple


print("\n Three print")


n=int(input("please enter the limit:"))


for i in range(1,n+1,3):
    print(i)





#Array

n=int(input("please enter the limit:"))

b=[]

for i in range(n):

    b.append(input())

print("\n given values")

for i in range(n):






#sum of Array

n=int(input("please enter the limit:"))

b=[]

sum=0

print("\n enter the values")
for i in range(n):

    b.append(int(input()))

print("\n given values")

for i in range(n):

    sum +=b[i]
print("sum of array:",sum)






# odd numbers and even number in array


n= int(input("please enter the limit:"))

a=[]

sum=0







print("\n enter the values:")


for i in range(n):

    a.append(int(input()))

print("\n given values")

print("\n odd numbers")

for i in range(n):

    if(i%2!=0):
        print("a[",i,"]=",a[i])

        sum+=a[i]

                                 

print("sum of even numbers:",sum)


        


print("\n even numbers")

for i in range(n):
    if(i%2==0):
        print("a[",i,"]=",a[i])

        sum+=a[i]

                                 

print("sum of odd numbers:",sum)
        

    





# array  insert in new value. 


n=int(input("please enter the limit:"))

a=[]

print("\n Enter the values:")

for i in range(n):

    a.append(int(input()))


for i in range(n):

    print("a[",i,"]=",a[i])


inx = int(input("plese enter the index:"))
val =int(input("please enter the value:"))


for i in range(n):

    if(i==inx):
        a.insert(inx,val)

print("Array insert")

for i in range(n):

    print("a[",i,"]=",a[i])




# array update new value..a

# array  insert


n=int(input("please enter the limit:"))

a=[]

print("\n Enter the values:")

for i in range(n):

    a.append(int(input()))


for i in range(n):

    print("a[",i,"]=",a[i])


inx = int(input("plese enter the index:"))
val =int(input("please enter the value:"))


for i in range(n):

    if(i==inx):
        #a.insert(inx,val)

        a[inx]=val


print("Array insert")

for i in range(n):

    print("a[",i,"]=",a[i])



    
#array delete..........


# array  insert


n=int(input("please enter the limit:"))

a=[]

print("\n Enter the values:")

for i in range(n):

    a.append(int(input()))


for i in range(n):

    print("a[",i,"]=",a[i])


inx = int(input("plese enter the index:"))



a.pop(inx)

    

print("Array Delete")

for i in range(n-1):

    print("a[",i,"]=",a[i])



    



    









    







    



    








    


