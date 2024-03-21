'''
__add__
__sub__
__mul__
__truediv__


'''







class employees:

    def __init__(self,name,salary):

        self.name=name
        self.salary=salary

        print("Name:",self.name)
        print("Salary:",self.salary)


class payroll:

    def __init__(self,days):

        self.days=days
        

obj1=employees("RenuVijay",25000)

obj2=payroll(30)

print(obj1.salary *obj2.days)

    

    



class employees:

    def __init__(self,name,salary):

        self.name=name
        self.salary=salary

        print("Name:",self.name)
        print("Salary:",self.salary)


    def __mul__(self,renu):

        return self.salary*renu.days



        

obj1=employees("RenuVijay",25000)

obj2=payroll(30)

print(obj1*obj2)

    

    
