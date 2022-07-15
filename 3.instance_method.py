#Instance method
class Student:
    name = "Alex britto"
    age = 22
    
    def printall(self,gender): #self => instance method(directah object use panni call pannalam)
        print("Name : ",Student.name)
        print("Age : ",Student.age)
        print("Gender : ",gender)

#example
o=Student()
'''
New style
o.printall()
Student.printall(o)
'''
o.printall("male")
#old dtyle
Student.printall(o,'Male')
-----------------------------------------------------------------------------
#output
Name :  Alex britto
Age :  22
Gender :  male
Name :  Alex britto
Age :  22
Gender :  Male