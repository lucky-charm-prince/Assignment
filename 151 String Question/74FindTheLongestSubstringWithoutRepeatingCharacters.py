# S = "abcabcbb"  output : "abc"


s=input("String : ")
s1=""
for i in range(len(s)):
    x=""
    for j in range(i,len(s)):
        if s[j] not in x:
            x+=s[j]
        else:
            break 
    
    if len(x)>len(s1):
        
        s1=x
print(s1)        

