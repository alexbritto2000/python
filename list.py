#List in python
'''
Sequence type
Mutable - Values can be changed
a[5]
a={1,2,3,4,5,6}
a[0]
'''
a = [1,2,3,4]
print(a)
a[0] = 100
print(type(a))
print('----Slicing----')
print(a[0:3])
print(a[1:])
print(a[:3])
print('----------------')
a = [1,True,'ALex',2.5,[1,2,3,4]]
print(type(a[2]),'string')
print(a[4][2],'Inner list')
print('----------Inbulit Functions-------------')
a = [10,20,30]
#a.clear()
print(a)
b = a.copy()
print(b)
a = [1, 3, 504, 3, 9, 3, 10]
print(a.count(3),'COUNT')
print(a.index(504),'INDEX')
print(len(a),'LENGTH')
print(max(a),'MAX')
print(min(a),'MIN')
print(a,'Before pop')
a.pop(0) #Remove element using index value
print(a,'After pop')
a = [1, 3, 504, 3, 9, 3, 10]
a.remove(3) #Remove values
print(a,'Remove')
print('----------------------------------------')
names=['alex']
print(names,'Before Append')
names.append('britto')
names.append('ram')
print(names,'After Append')
names2=['lee', 'kilo']
names.extend(names2)
print(names,'Extend --> merge 2 lists ')
names.append('kumar')
names.insert(0,'surya')
print(names,'Insert')
print('--------------List Construtor------------------')
print(list(range(5)))
print(list('alexbritto'))
a = [10,50,100,25,85]
print(a,'Before sort')
a.sort()
print(a,'After sort')
a.sort(reverse=True)
print(a,'Reverse')
a=['Apple','orange','banana']
a.sort()
print(a,'sort')
a=['Apple12','orange','banana']
a.sort(key=len)
print(a,'sort using len')
#output
[1, 2, 3, 4]
<class 'list'>
----Slicing----
[100, 2, 3]
[2, 3, 4]
[100, 2, 3]
----------------
<class 'str'> string
3 Inner list
----------Inbulit Functions-------------
[10, 20, 30]
[10, 20, 30]
3 COUNT
2 INDEX
7 LENGTH
504 MAX
1 MIN
[1, 3, 504, 3, 9, 3, 10] Before pop
[3, 504, 3, 9, 3, 10] After pop
[1, 504, 3, 9, 3, 10] Remove
----------------------------------------
['alex'] Before Append
['alex', 'britto', 'ram'] After Append
['alex', 'britto', 'ram', 'lee', 'kilo'] Extend --> merge 2 lists 
['surya', 'alex', 'britto', 'ram', 'lee', 'kilo', 'kumar'] Insert
--------------List Construtor------------------
[0, 1, 2, 3, 4]
['a', 'l', 'e', 'x', 'b', 'r', 'i', 't', 't', 'o']
[10, 50, 100, 25, 85] Before sort
[10, 25, 50, 85, 100] After sort
[100, 85, 50, 25, 10] Reverse
['Apple', 'banana', 'orange'] sort
['orange', 'banana', 'Apple12'] sort using len