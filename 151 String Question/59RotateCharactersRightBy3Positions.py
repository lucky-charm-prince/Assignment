# S = "abcde" output :- "cdeab"

s=input("String : ")
l=len(s)
s1=s[l-3:l]
s2=s[0:l-3]
s3=s1+s2
print(s3)