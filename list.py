# list 

'''
it can alow duplicates 
and includes all data types

append,clear,copy,index,insert,count,pop,remove,reverse,sort
'''

print(list)
lst =["renu",10,20,30,20,40,10.4,10+5j]

print(lst)

print("\n")

lst =["renu",10,20,30]

lst.append(10)
print("Append:",lst)


print("\n")

lst.clear()
print("clear:",lst)


# copy

lst =[10,20,30]

ls=lst.copy()
print("copy:",ls)


#count

lst =[10,20,20,30,20]

c=lst.count(20)

print("count:",c)


# index

lst =[10,20,20,30,20]

c=lst.index(20)

print("index:",c)


# insert

lst =[10,20,20,30,20]

lst.insert(2,200)

print("insert:",lst)


# pop
lst =[10,20,20,30,20]

lst.pop()

print("index:",lst)


 # remove

lst =[10,20,20,30,20]

lst.remove(10)

print("Remove:",lst)



# reverse

st =[10,20,20,30,20]

st.reverse()

print("index:",st)


# sort

st = [10,20,20,30,20]

st.sort()

print("Sort:",st)









