# S = "the cat and the dog"  output :- "the cat and dog"

s=input("String : ")
l=len(s)
s1=""
start=0
for i in range(l):
    if s[i]==' ':
        if s[start:i]+" " not in s1:
            s1+=s[start:i]+" "
        start=i+1
else:
    if s[start:]+" " not in s1:
        s1+=s[start:]
print(s1)        