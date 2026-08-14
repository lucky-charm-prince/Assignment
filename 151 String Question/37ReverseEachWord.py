# S = "cat dog"  output:- "tac god"

s=input("String : ")
l=len(s)
s1=""
start=0
for i in range(l):
    if s[i]==' ':
        word=s[start:i]
        start=i+1
        newWord=""
        for j in word:
            newWord=j+newWord
        s1+=newWord+" "
else:
    word=s[start:l]
    newWord=""
    for j in word:
        newWord=j+newWord
    s1+=newWord
print(s1)    
    

                