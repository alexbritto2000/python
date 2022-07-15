#class and attribute
class car():
    pass
a=10
print(type(a))
print(type(car))
swift=car()
print(isinstance(swift,car))
print(isinstance(a,int))
print(type(swift))

class Student():
    name = "Ram"
    age = 25
#name and age are class attribute
#getattr method
print(getattr(Student,'name'))
print(getattr(Student,'gender','No such attribute found'))

#DOt notation
print(Student.name)
print(Student.age)
#Setattr
setattr(Student,'name','Alex')
print(Student.name)
setattr(Student,'gender','Male')
print(Student.gender)

Student.city="salem"
print(Student.city)
#print(Student.__dict__)
delattr(Student,"city")
#print(Student.__dict__)
del Student.gender
-------------------------------------------------------------
#output
<class 'int'>
<class 'type'>
True
True
<class '__main__.car'>
Ram
No such attribute found
Ram
25
Alex
Male
salem
----------------------------------------------------------------