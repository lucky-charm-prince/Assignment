# S = "find the longest word" output :-  "longest"

s=input("String : ")
l1=len(s)
word=""
l2=0
start=0
for i in range(l1):
    if s[i]==' ':
        if i-start>l2:
            word=s[start:i]
            l2=len(word)
        start=i+1
else:
    if l1-start>l2:
        word=s[start:l1]            
        l2=len(word)
print(word)        