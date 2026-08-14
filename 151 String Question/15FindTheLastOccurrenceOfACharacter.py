s=input("Enter the String : ")
c=input("Enter teh Char : ")
for i in range(len(s)-1,-1,-1):
    if c==s[i]:
        print(i)
        break
else:
    print("NOt Found ")
