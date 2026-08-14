# S = "apple banana apple" output:- apple: 2, banana: 1
s2=input("String : ")

s1=""
start=0
s=s2+" "
l=len(s)
for i in range(l):
    if s[i]==' ':
        y=s[start:i]
        x=" "+s[start:i]+" "
        if  x not in s1:
            
            count=1
            s1+=" "+x+" "
            temp=i+1
            for j in range(i+1,l):
                if s[j]==' ':
                    if  s[temp:j]==y:
                        count+=1
                    temp=j+1
            print(y,count)                    
        start=i+1
        
