#functions
def welcome():
    print("Hello world")
welcome()
#1.No return without argument
def add():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    c=a+b
    print("Total:", c)
add()
#2.No return with argument
def sub(a,b):
    c=a-b
    print("Difference:",c)
sub(25,2)
#3.return with argument
def mul():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    c=a*b
    return c
print("Mul",mul())
 -----------------------------------------------------------------
#4.Arbitary function
#can pass unlimitted arguments
def class_10(*students):
    print(students)
class_10("ram","alex","britto")

#5.keyword arguments in python
def message(name,age):
    print(name,"age is ",age)
message(name="Ram", age=24)

#6.Arbitary keywords arguments in python
def bioData(**data):
    print(data)
bioData(name="alex",age=22,gender="Male")

#7.default parameter function
def user(name,city="salem"):
    print(name,'is from ',city)
user("Ram","namakkal")
user("sam")

#8.Passing list as arguments
def total(marks):
    return sum(marks)
print("Total:",total([100,80,90,70,98]))

#9.Recursive function(function work ah mudikka again athaiye call pannichina recursive function)
#1*2*3*4*5
def factorial(x):
    if (x==1):
        return 1
    else:
        return(x*factorial(x-1))
print("Factorial: ",factorial(5))
'''
factorial(5)
5*factorial(4)
5*4factorial(3)
5*4*3factorial(2)
5*4*3*2factorial(1)
5*4*3*2*1
120
'''

#10.Lambda function(Anonymus function)-name illa function
c=lambda a: a+50
print(c(5))
c=lambda a,b: a+b
print(c(10,20))

#output
('ram', 'alex', 'britto')
Ram age is  24
{'name': 'alex', 'age': 22, 'gender': 'Male'}
Ram is from  namakkal
sam is from  salem
Total: 438
Factorial:  120
55
30
-----------------------------------------------------------------------------------