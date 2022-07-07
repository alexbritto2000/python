#Tuple
#Immutable = can't change
#Surrounded bu round bracs(1,1,2)

a = (1,2.3,True,'alex')
print(a)
print(type(a))
print(a[0])
print(a[-1])
print(a[0:2])
b = list(a)
print(b,'convert to list')
print(type(b))
b.append('alex')
print(b)
a=tuple(b)
print(a)
print(type(a))
print('-------------------')
for i in a:
    print(i)
if 'alex' in a:
    print("alex is found")
else:
    print("Not Found")
print('--------------------')
print(len(a),'length')
a=(2,)
print(type(a))
del a
a=(1,2,3,4,5)
b=(6,7,8,5,10)
c=a+b
print(c)
print(c.count(5),'count')
print('-------Nested Tuples--------')
a=(1,2,3,4,5)
b=(6,7,8,5,10)
c=(a,b)
print(c,'Nested tuples')
print(c[0][1])
x=('alex, ')*10
print(x)
#ouput
(1, 2.3, True, 'alex')
<class 'tuple'>
1
alex
(1, 2.3)
[1, 2.3, True, 'alex'] convert to list
<class 'list'>
[1, 2.3, True, 'alex', 'alex']
(1, 2.3, True, 'alex', 'alex')
<class 'tuple'>
-------------------
1
2.3
True
alex
alex
alex is found
--------------------
5 length
<class 'tuple'>
(1, 2, 3, 4, 5, 6, 7, 8, 5, 10)
2 count
-------Nested Tuples--------
((1, 2, 3, 4, 5), (6, 7, 8, 5, 10)) Nested tuples
2
alex, alex, alex, alex, alex, 
> 