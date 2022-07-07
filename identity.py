#Rendu object ah compare panni equal la irukka ntu check panni sollum
'''
is
is not
'''
a=[1,2]
b=[1,2]
c=a
print(id(a))
print(id(c))
print(id(b))
print(a is c)
print(a==b)
print(a is b)
print(a is not b)
print(a!=b)

#ouput
139802735664832
139802735664832
139802735028608
True
True
False
True
False