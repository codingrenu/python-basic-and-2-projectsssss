'''
exception handling is 158 currently they areusing to solve errors they are mainly used in 6types of errors

else blockand try blockcan print the output and finally is always run its mainly

use in database queries.


'''




# Exception handling.

a=dir(locals()['__builtins__'])

print((a))

print(len(a))


#1.............

try:
    a=10
    b=2
    c=a/b
    print(c)

    

except exception  as e:

    print(e)
    
#2. Zero division error.............
    
try:
    a=10
    b=0
    c=a/b
    print(c)

    

except ZeroDivisionError  as e:

    print(e)




    
#2. Zero division error.............
    
try:

   name="Renu Vijay"

   print(age)



except NameError as e:

    print("ERROR:",e)




#3. Value error.............
    
try:

   num =int(input("please enter the number:",))

   print(num)
   

            


except ValueError as e:

    print("ERROR:",e)


#4. index error.............

try:
    lst=[10,20,30,40,50]
    print(lst[6])


    
except IndexError as e:
    print("indexerror:",e)


#5. key error.............

try:

    dic={"Name":"renu vijay","age":23}

    print(dic['address'])


    
except KeyError as e:
    print("indexerror:",e)


#6. Attribute error.............

try:

    class renu:
        
        def daniel(self):
            print("result:","hai how are you")
    m=renu()
    m.daniel()




except AttributeError as e:
    print("ATRRIBUTE Error:",e)

    



#1. else and finally

#1.............

try:
    a=10
    b=0
    c=a/b
    

    

except exception  as e:

    print("error:",e)



else:
    print("value:",c)

finally:

    print("programs end")
    
