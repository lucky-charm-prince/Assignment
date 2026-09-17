# Char[] = {'h', 'i'} output :- "hi"

list=[]
s=""
n=int(input("Size : "))
for i in range(n):
    temp=input("Char : ")
    s+=temp
    list.append(temp)
print(list)    
print(s)
    


