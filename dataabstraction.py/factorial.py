# data abstraction
'''
data abstrction is hide the date in the hidden from the users.

'''

class factorial:

    def fact(self,num):
        
        f=1
        
        for i in range(1,num+1):
            
            f*=i
            
        return f
