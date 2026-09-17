# S = "a1b2c3" output : 6 (1+2+3)

total=0
s=input("String : ")
for i in s:
    if '0'<=i<='9':
        total+=int(i)
print(total)        

