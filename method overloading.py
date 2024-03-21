'''
polymorphisim means many forms

it can use same functions but use differentarguments is called method overloading
(or) function over loading.





class myclass:

    def fun(self,a):

        print(a)

    def fun(self,a,b):

        print(a+b)

                           ......................notstable usein method overloading.
    def fun(self,a,b,c):

        print(a+b+c)


s=myclass()
s.fun(10,20,30)

'''

# method overloading

class myclass:



    def fun(self,a=None,b=None,c=None):

        if (a!=None and b!=None and c!=None):

            print("Result:",a+b+c)


        
        elif(a!=None and b!=None):
             print("Result:",a+b)

        else:

            return a
        
        

        

h=myclass()
h.fun(10,20,30)


# multiple args use inmethodover loading:

class loading:

    def multiple(self,*args):

        sum=0

        for data in args:

            sum+=data
            
        print("Result:",sum)

u=loading()
u.multiple(10,20,30,40)
            






        







