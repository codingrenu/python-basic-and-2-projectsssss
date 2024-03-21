# python memory location
a=24
b=a

print(id(a))
print(id(b))

a=55
print(id(a))


x=y=z=50
print(id(x))
print(id(y))
print(id(z))

a,b,c=2,3,4
print(id(a))
print(id(b))
print(id(c))



# importkeyword

import keyword

print(keyword.kwlist)




#datatypes 

a=34
b=35.0
c="cf"
d='dd'


print(type(a))
print(type(b))
print(type(c))
print(type(d))



c=1+5j
print(type(c))
print("c is a complex number",isinstance(1+5j,complex))



#del
'''
c=45

print(c)

del c

print(c)
'''



a1=23
b1=23

d1=45
d2=88

cc=23
dc=23


print(a1 is not b1)



# single line comment

'''basic.py''' # multiline comment