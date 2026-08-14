# S = "a test b test c", Word = "test", Remove All  output :- "a b c"

s=input("String : ")
l1=len(s)
word=input("Word : ")
l2=len(word)
start=0
s1=""
for i in range(l1):
    if s[i]==' ':
        if  i-start!=l2 or word!=s[start:i]:
            s1+=s[start:i]+" "
        start=i+1
else:
    if l1-start!=l2 or word!=s[start,l1]:
        s1+=s[start:]
print(s1)                
