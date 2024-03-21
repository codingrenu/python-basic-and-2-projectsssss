'''
set is one of the data types in python.
it can intialise in using in curly brackets.

a={10,20,'C',   "Renu',10+5j,10}

it not allowed duplicates.

outpt can displayed in unarranged format

especially descending order format.


set functions

add()
copy()
update()
clear()
remove()
discard()
pop()

'''


print("SET")
print("\n")

a={10,20,30,10,"ram",'c',10+5j}

print("SET:",a)


print("\n")

a={10,20,30,10,"ram",'c',10+5j}

a.add(200)

print("ADD",a)


print("\n")

a={10,20,30,10,"ram",'c',10+5j}
c=a.copy()
print("COPY:",c)


print("\n")

a={10,20,30,10,"ram",'c',10+5j}

b={300,"daniel"}

a.update(b)
print("update:",a)

print("\n")

a={10,20,30,10,"ram",'c',10+5j}

c=a.clear()
print("clear:",c)


print("\n")

b={10,20,30,10,"ram",'c',10+5j}

b.remove(30)
print("REMOVE:",b)


print("\n")

b={10,20,30,10,"ram",'c',10+5j}

b.discard(20)
print("discard:",b)


print("\n")

b={10,20,30,10,"ram",'c',10+5j}

b.pop()
print("pop:",b)












