# Strings = ["flower", "flow", "flight"]  output: "fl"
import sys
s=[]
n=int(input("Size : "))
l="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
for i in range(n):
    x=input("Value")
    
    if len(x)<len(l):
        l=x
    s.append(x)
print(s)    
x=0

for i in range(len(l)):
    x=l[0:len(l)-i]
    for j in range(n):
        if s[j][0:len(x)]!=x:
            break
    else:
        print(x)
        break
        


    

        
