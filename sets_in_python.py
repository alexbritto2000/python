names={'Ram', 'Sam', 'Ravi'}
print(names)
print(type(names))

#Access values using for loop
#can we add new name but can't change existing name
for name in names:
    print(name)

#Adding new element
names.add('sara')
print(names)

#update another set of data
a={'kumar','sunder','suresh'}
names.update(a)
print(names)

#remove name
names.remove('sara')
print(names)

#discard
names.discard('alex')
print(names)

#in set pop delete random one name
names.pop()
print(names)

names.clear()
print(names)

#delete whole set
del names
print(names)

#output
{'Ravi', 'Ram', 'Sam'}
<class 'set'>
Ravi
Ram
Sam
{'Ravi', 'Ram', 'sara', 'Sam'}
{'Ravi', 'Ram', 'sunder', 'kumar', 'suresh', 'sara', 'Sam'}
{'Ravi', 'Ram', 'sunder', 'kumar', 'suresh', 'Sam'}
{'Ravi', 'Ram', 'sunder', 'kumar', 'suresh', 'Sam'}
{'Ram', 'sunder', 'kumar', 'suresh', 'Sam'}
set()
Traceback (most recent call last):
  File "<string>", line 36, in <module>
NameError: name 'names' is not defined

---------------------------------------------------------------------------------------------------------------

#set automatically delete duplicate values
#if we want to get unique data can we pass data into set constructor
names={'Ram', 'Ram', 'Sam', 'Ravi','alex','britto'}
print(names)

#output
{'Ram', 'alex', 'Ravi', 'Sam', 'britto'}

-----------------------------------------------------------------------------------------------------------------

#union
a={1,2,3,4,5}
b={'a','b','c','d'}
c=a.union(b)
print(c)

#update
a.update(b)
print(a)

#intersection=common values
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

#symitric difference
a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

#disjoint
a={1,2,3,4}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)

#subset
a={5,6,7,}
b={5,6,7,8,9}
c=a.issubset(b)
print(c)

#superset
a={5,6,7,8,9}
b={5,6,7}
c=a.issuperset(b)
print(c)

#ouput
{1, 2, 3, 4, 5, 'b', 'c', 'd', 'a'}
{1, 2, 3, 4, 5, 'b', 'c', 'd', 'a'}
{5}
{5}
{1, 2, 3, 4, 6, 7, 8, 9}
{1, 2, 3, 4, 6, 7, 8, 9}
True
True
True

-----------------------------------------------------------------------------------------------------