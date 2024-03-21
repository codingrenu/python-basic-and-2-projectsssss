from factorial import *

num =int(input("please enter thefactorial number:"))

obj =factorial()

res=obj.fact(num)

print("the factorial",num,"is:",res) \



#data abstraction exapmle program employee management. 



'''
class employees:

    def add_employee(self):
        pass

    def view_employee(self):
        pass

    def Remove_employee(self):
        pass

obj=employees()

while True:

    print("\n")

    print("1.Add employee")
    print("2.viewemployee")
    print("3.Delete employee")
    print("4.Exit")


    data=int(input("please enter your choice:"))


    if(data==1):
        obj.add_employee()

    elif(data==2):
        obj.view_employee()

    elif(data==3):
        obj.Remove_employee()

    else:
        exit()
'''

class employees:

    def add_employee(self):
        self.emp=[]
        count=int(input("\n How many employees would like to add:"))

        print("\n print the employees name:")

        for i in range(count):
            
            ename=input()

            self.emp.append(ename)
            

    def view_employee(self):
        
        print("\n List the number of employees:")

        for sno,name in enumerate(self.emp,1):
            
            print("{}.{}" .format(sno,name))
        
    def Remove_employee(self):
        
        data=(input("\n Which employee you want to delete:"))

        if data in self.emp:

            self.emp.remove(data)
            print("Employee deleted")

        else:
            print("Invalid employee name...!!!")
            

obj=employees()

while True:

    print("\n")

    print("1.Add employee")
    print("2.viewemployee")
    print("3.Delete employee")
    print("4.Exit")


    data=int(input("please enter your choice:"))


    if(data==1):
        obj.add_employee()

    elif(data==2):
        obj.view_employee()

    elif(data==3):
        obj.Remove_employee()

    else:
        exit()




        




        

