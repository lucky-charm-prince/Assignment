s=input("String : ")

l1=len(s)
word=input("word : ")
l2=len(word)
start=0
for i in range(0,l1):
    if s[i]==' ':
        if i-start==l2 and word==s[start:i]:
            print(start)
            break
        start=i+1
else:
    if l1-start==l2 and word==s[start:]:
        print(start)
    else:
        print("not found")              