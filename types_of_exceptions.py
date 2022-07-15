#Types of exception
#print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

#1.Name error exception
try:
    print(a)
except NameError as e:
    print("A is not defined")

#2.ZeroDivisionError 
try:
    print(10/0)
except ZeroDivisionError as e:
    print("Denominator cant be zero")

#3.ValueError
try:
    a=int("alex")
except ValueError as e:
    print("Please Enter Numbers Only")
    
#4.Index out of bound
try:
    a=[10,20,30,40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")
    
#5.File not found
try:
    f=open('text.txt')
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
    
#6.Multiple Exception
try:
    a=16/20
    print(a)
    b=[10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print("Denominator cant be zero")
except IndexError:
    print("Invalid Index")
-------------------------------------------
#output
152
A is not defined
Denominator cant be zero
Please Enter Numbers Only
Invalid Index
File not found
0.8
Invalid Index
> ----------------------------------------