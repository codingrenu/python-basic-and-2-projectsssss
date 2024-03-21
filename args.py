'''

args, and kwargscn use in mutile time use purpose in function

*args
**kwargs

'''

def  fun(a,b,c):
    

    d=a+b+c
    print(d)
fun(10,20,30)



#01 .multiple agrument used in function use *args
'''
def  fun(*args):
    sum=0
    for data in args:
        sum+=data
        
    print("result:",sum)
fun(10,20,30,40)
'''

#01 .multiple agrument used in function use *args

def  fun(**kwargs):
    
   for key,value in kwargs.items():
   
       print("%s:%s"%(key,value))

fun(name="Renu",Age=24,Address="singrapettai")
    
    
        
    
fun(10,20,30,40)
