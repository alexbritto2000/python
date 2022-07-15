class user:
    course = 'Java'
    
o = user()
print(user.__dict__)
print(user.course)    #print class attribute
print(o.__dict__)
print(o.course)

o.course = "c++"
print(o.__dict__)
print(o.course)
o2 = user()
print(o2.course)
--------------------------------------------------------------------------------------
#output
{'__module__': '__main__', 'course': 'Java', '__dict__': <attribute '__dict__' of 'user' objects>, '__weakref__': <attribute '__weakref__' of 'user' objects>, '__doc__': None}
Java
{}
Java
{'course': 'c++'}
c++
Java
---------------------------------------------------------------------------------------