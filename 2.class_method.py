#class ah use panni functionah call panrom
class Student:
    name = "Alex britto"
    age = 22
    
    def printall():
        print("Name : ",Student.name)
        print("Age : ",Student.age)

Student.printall()
print(Student.__dict__)
print(getattr(Student,"printall"))
getattr(Student,"printall")()
Student.__dict__['printall']()
-------------------------------------------------------------------------
#output
Name :  Alex britto
Age :  22
{'__module__': '__main__', 'name': 'Alex britto', 'age': 22, 'printall': <function Student.printall at 0x7f80bbc7edc0>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
<function Student.printall at 0x7f80bbc7edc0>
Name :  Alex britto
Age :  22
Name :  Alex britto
Age :  22
--------------------------------------------------------------------------