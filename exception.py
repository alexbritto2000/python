#try block in python
#1.compile time error
#2.Run time error
'''
try:
    a=10/0
except Exception as e:
    print(e)

try:
    a=10/1
except Exception as e:
    print(e)
else:
    print("A value : ",a)
'''

try:
    a=10/0
except Exception as e:
    print(e)
else:
    print("A value : ",a)
finally:
    print("Thank you")
------------------------------------
#output
division by zero
Thank you
------------------------------------