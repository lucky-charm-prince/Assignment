# Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"

list=[]
str=""
n=int(input("Size : "))
for i in range(n):
    temp=int(input("ord value : "))
    str+=chr(temp)
    list.append(temp)
print(list)    
print(str)


