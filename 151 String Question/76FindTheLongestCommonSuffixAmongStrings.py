# Strings = ["baking", "making", "taking"] output: "king"

import sys
s=[]
n=int(input("Size : "))
l=None
for i in range(n):
    x=input("Value")
    if l==None:
        l=x
    if len(x)<len(l):
        l=x
    s.append(x)
print(s)    
x=0


for i in range(len(l)):
    x = l[::-1]
    x=x[:len(x)-i]
    
    for j in range(n):
       temp=s[j]
       temp=temp[::-1]
       if temp[:len(x)]!=x:
           break
    else:
        print(x[::-1])
        break
        
