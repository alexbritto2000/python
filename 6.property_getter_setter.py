#Property Decorator getter setter
#Encapsulation
class Student:
    def __init__(self,total):
        self._total=total #self._total => private variable ah act aagum
    def average(self):
        return self._total/5.0
        
    @property
    def total(self):
        return self._total
        
    @total.setter
    def total(self,t):
        if t<0 or t>500:
            print("Invalid total and can't change")
        else:
            self._total=t
        
o=Student(450)
print("Total   : ",o.total)
print("Average : ",o.average())
o.total = 432
print("Total   : ",o.total)
print("Average : ",o.average())
------------------------------------------------------------------
#output
Total   :  450
Average :  90.0
Total   :  432
Average :  86.4