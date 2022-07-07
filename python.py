#cmd
-------------------
1.run = python file_name.py
2.clear address=echo off
3.clear screen=cls
-------------------
#1.type and id
------------------------
a = 10
b = 20
c = a+b
print('total:',c)
a = 40
print(type(a))
print(id(a))
print(id(b))
print(id(c))
-----------------------
#output
Hello world
total: 30
<class 'int'>
9789280
-------------------------
#2.keyword list
--------------------------
import keyword
print(keyword.kwlist)
---------------------------------------------------------------------------
#output
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 -----------------------------------------------------------------------------
 #3.input
 --------------------------------------------------------------------------
name=input('Enter your name:')
print('Hii',name)
print(type(name))
#output
Enter your name:alex
Hii alex
<class string>

a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
c=a+b
print('Total:',c)
#output
Enter value of A:5
Enter value of B:7
Total: 12
------------------------------------------------------------------------
#3.1.Multiple inputs
-----------------------------------------------------------------
name1,name2,name3=input('Enter 3 names:').split(',')
print('Name1:',name1)
print('Name2:',name2)
print('Name3:',name3)
#output
Enter 3 names:alex,britto,sab
Name1: alex
Name2: britto
Name3: sab
-----------------------------------------------------------------------
#3.2.input para
---------------------------------------------------------------------------------------------
a="""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type specimen book.
"""
print(type(a))
print(a)
-------------------------------------------------------------------------------------------------
#output
<class 'str'>

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
---------------------------------------------------------------------------------------------------
#3.2.1.input para
----------------------------------------------------------------------------------------------------
para1=['1','2','3']
print('|'.join(para1))
print(para1)

para=[]
print('Enter a para:')
while True:
  line=input()
  if line:
    para.append(line)
  else:
    break
print(para)
output='\n'.join(para)
print(output)
#output
1|2|3
['1', '2', '3']
Enter a para:
I am alex
I was 22 years old

['I am alex', 'I was 22 years old']
I am alex
I was 22 years old
--------------------------------------------------------------------------------------------------
#4.string handling(type casting-change type of varables)
----------------------------------------------------------------------------------------------------
print("Hello world")
s = "Tutor Joes"
print(s)
print(type(s),':type')
print(s.upper(),':upper')
print(s.lower(),':lower')
print(s.capitalize(),':capitalize')
print(s.title(),':title')
print(s.count('t'),':count')
print(s.endswith('es'),':endswith')
print(s.find('t'),':find')
print(s.replace('o','7'),':upper')
a = 'JOES'
print("Is Upper: ",a.isupper())
print("Is Lower: ",a.islower())

s="he\nis\ngood"
print(s.splitlines())
print(s.splitlines(True))
a = "Tutorjoes,computer education"
print(a.split(","))
print('Remove white space')
b = "     joes    "
print(len(b))
print(len(b.strip()))
print('Remove white space in left')
print(len(b.lstrip()))
c = "17-04-2000"
print(c.partition('-'))
#output
Hello world
Tutor Joes
<class 'str'> :type
TUTOR JOES :upper
tutor joes :lower
Tutor joes :capitalize
Tutor Joes :title
1 :count
True :endswith
2 :find
Tut7r J7es :upper
Is Upper:  True
Is Lower:  False
['he', 'is', 'good']
['he\n', 'is\n', 'good']
['Tutorjoes', 'computer education']
Remove white space
13
4
Remove white space in left
8
('17', '-', '04-2000')
---------------------------------------------------------------------------------------------------------
#4.1 String Manipulation
---------------------------------------------------------------------------------------------------------
'''
s  a  m  p  l  e
0  1  2  3  4  5 
-6 -5 -4 -3 -2 -1
'''
s="sample"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[:-1])
print(s[::-1])
#output
sample
sa
sampl
ample
e
l
sampl
elpmas
-------------------------------------------------------------------------------------------------------------
#5.Arithmatic Oprators
-------------------------------------------------------------------------------------------------------------
"""
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
** Exponentiation
// Floor Division
"""
a = 123
b = 10
print(a + b,'Addition')
print(a - b,'Subtraction')
print(a * b,'Multiplication')
print(a / b,'Division')
print(a // b,'Floor Division')
print(a % b,'Modulus')
print(2**3,'Exponentiation')
#output
133 Addition
113 Subtraction
1230 Multiplication
12.3 Division
12 Floor Division
3 Modulus
8 Exponentiation
----------------------------------------------------------------------------------------------------
#5.1 Comparison Operators or Relational Operators
----------------------------------------------------------------------------------------------------
"""
==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to

"""
a = 20
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
#output
True
False
False
False
True
True
---------------------------------------------------------------------------------------------------
#5.2 Logical Operators in Python
----------------------------------------------------------------------------------------------------
"""
and
or
not

"""
a = 25
print(a >= 10 and a <= 20)
print(a >= 10 or a <= 20)
print(not(a >=  10 and a <= 20))
#output
False
True
True
------------------------------------------------------------------------------------------------------
