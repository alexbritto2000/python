#init method(constructor)
class user:
    def __init__(self,name):   #self => instanse attribute => self athoda class ke value new ah kudukka use panrom
        print("Call when new instance is created")
        self.name=name
    def printall(self):
        print("Name : ",self.name)
        
o=user("Alex Britto")
o.printall()
print(o.__dict__)
o1=user("Abcd")
o1.printall()
print(o1.__dict__)
---------------------------------------------
#output
Call when new instance is created
Name :  Alex Britto
{'name': 'Alex Britto'}
Call when new instance is created
Name :  Abcd
{'name': 'Abcd'}