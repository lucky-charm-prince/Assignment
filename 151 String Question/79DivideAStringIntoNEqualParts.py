# S = "abcdef", n = 3  output :- "ab", "cd", "ef"

s=input("String : ")
n=int(input("Enter the number of chunks : "))

num=len(s)//n
x=0
y=num

print(num)
for i in range(n):
    print(s[x:y],end=" , ")
    x=y
    y+=num
print(s[x:])    
