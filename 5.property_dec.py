#Property Decorator
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.msg=self.name+" is "+str(self.age)+" years old"
    @property
    def msg(self):
        return self.name+" is "+str(self.age)+" years old"
        
o=user("alex",22)
print(o.name)
print(o.age)
#decorator use pannathu nala function use panna venam
print(o.msg)
o.age=23
#age mattum update aagum
print(o.msg)
----------------------------------------------------------
#output
alex
22
alex is 22 years old
alex is 23 years old