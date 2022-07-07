#keys can't set duplicate values
user={
    'name':'Ram',
    'age':22,
    'isMarried':True
}
print(user)
print(type(user))
print(user['name'])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x," ",user[x])
print('---------------')
for x in user.values():
    print(x)
print('----------------')
for x in user.keys():
    print(x)
print('----------------')
for x,y in user.items():
    print(x,y)
print('---------------')
if 'age' in user:
    print('present')
print('---------------')

#changing values
user.update({
    'gender':'male'
})
print(user)

user['age']=35
print(user)

#remove age
user.pop('age')
print(user)

#clear all data
user.clear()
print(user)

#delete user dict
#del user
#print(user)

#nested dictionary
users={
    'user1':{ 'name':'alex', 'age':22, 'isMarried': True},
    'user2':{ 'name':'britto', 'age':25, 'isMarried': False}
}
print(users)

#ouput
{'name': 'Ram', 'age': 22, 'isMarried': True}
<class 'dict'>
Ram
22
dict_keys(['name', 'age', 'isMarried'])
dict_values(['Ram', 22, True])
dict_items([('name', 'Ram'), ('age', 22), ('isMarried', True)])
name   Ram
age   22
isMarried   True
---------------
Ram
22
True
----------------
name
age
isMarried
----------------
name Ram
age 22
isMarried True
---------------
present
---------------
{'name': 'Ram', 'age': 22, 'isMarried': True, 'gender': 'male'}
{'name': 'Ram', 'age': 35, 'isMarried': True, 'gender': 'male'}
{'name': 'Ram', 'isMarried': True, 'gender': 'male'}
{}
{'user1': {'name': 'alex', 'age': 22, 'isMarried': True}, 'user2': {'name': 'britto', 'age': 25, 'isMarried': False}}
---------------------------------------------------------------------------------------------------------------------------