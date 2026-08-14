# S = "a b c" outputl :-"c b a"
s=input("String : ")
l=len(s)
s1=""
start=0
for i in range(l):
    if s[i]==' ':
        word=s[start:i]
        for j in range(len(word)-1,-1,-1):
            s1=s1+word[j]
        s1=s1+" "
        start=i+1
else:
    word=s[start:l]
    for j in range(len(word)-1,-1,-1):
        s1=s1+word[j]
s2=""
for i in s1:
    s2=i+s2                    
print(s2)    
