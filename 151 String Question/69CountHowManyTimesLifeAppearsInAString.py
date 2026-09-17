# S = "life is life" output : 2
count=0
s=input("String : ")
s1="life"
for i in range(len(s)-len(s1)+1):
    if s[i:i+len(s1)]==s1:
        count+=1
print(count)        