# S = "abab", Sub = "ab"  output : 2
s=input("Strig")
s1=input("Sub String")
count=0
for i in range(len(s)-len(s1)+1):
    if s[i:i+len(s1)]==s1:
        count+=1
print(count)        