"""
 
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Numbe"""


no=int(input("enter the no="))
square=no**2
temp=0 
modu=(len(str(no)))
org=no

"""

for i in range(len(str(no))):
    if i==(len(str(no)))-1:
       temp=square%10**modu
       print(temp)
    
if temp==no:
   print("automrphic number")
else:
   print("not automrphic number") """

       
while no>0 :
    if no==square%10**modu:
       temp=square%10**modu
    no=no//10
if temp==org:
   print("automrphic number")
else:
   print("not automrphic number")
    