# S = "this madam is here" output:- "madam"

s=input("String : ")
l=len(s)
start=0
for i in range(l):
    if s[i]==' ':
        word=s[start:i]
        
        for j in range(len(word)//2+1):
            if word[j]!=word[len(word)-1-j]:
                break
        else:
            print(word)
            break
        start=i+1    
else :
    word=s[start:l]
    
    for j in range(len(word)//2+1):
        if word[j]!=word[len(word)-1-j]:
            break
    else:
        print(word)
        

