# S = "old data", Old="old", New="new"  output :- "new data"

s=input("String : ")
l1=len(s)
Oldword=input("OldWord : ")
l2=len(Oldword)
newWord=input("NewWord : ")
start=0
s1=""
for i in range(l1):
    if s[i]==' ':
        if i-start==l2 and s[start:i]==Oldword:
            s1+=newWord+" "
        else:
            s1+=s[start:i]+" "    
        start=i+1
else:
    if l1-start==l2 and s[start:l1]==Oldword:
        s1+=newWord
    else:
        s1+=s[start:]    
print(s1)        


