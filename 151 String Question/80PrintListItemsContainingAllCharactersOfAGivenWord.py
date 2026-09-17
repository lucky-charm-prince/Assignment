# List = ["apple", "plea"], Word = "pal" output:- "apple", "plea"

list=[]
n=int(input("Number of Element : "))
for i in range(n):
    s=input("Values : ")
    list.append(s)

print(list)

str=input("Enter the Word : ")

for i in list:
    for j in str:
        if j not in i:
            break
    else:
        print(i,end=" , ")    
        
