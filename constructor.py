#constructor

'''
constructor is ia build in function itsonly declare is  ok notto calling is
unnecessary.

def __init__(self):

'''

class constructor:

    def __init__(self,name,age,address,email,contact):

        self.Name=name
        self.Age=age
        self.Address=address
        self.Email=email
        self.Contact=contact

        print("\n this is inbuild so don't need to object calling")
        

        print("Name:",name)
        print("Age:",age)
        print("Address:",address)
        print("Email:",email)
        print("Contact:",contact)

        print("\n this is in user defined  so  need to object calling")
        

    def daniel(self):
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Address:",self.Address)
        print("Contact:",self.Email)
        print("Contact:",self.Contact)
        
        
        



ob=constructor("renu vijay",23,"singarapettai","kit.24.22mmc041@gmail.com",9003944506)
ob.daniel()
        
