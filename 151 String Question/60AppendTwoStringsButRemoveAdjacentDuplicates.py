# S1="miss", S2="issippi" output:- "misisipi"

s1=input("String 1 : ")
s2=input("String 2 : ")
s3=s1+s2

x=s3[0]
for i in range(1,len(s3)):
    if s3[i]!=x[len(x)-1]:
        x+=s3[i]
print(x)        