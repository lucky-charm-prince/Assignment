# S = "banana", Char='a'  output:- 1, 3, 5 (indices)

s=input("String : ")
l=len(s)
ch=input("Char : ")
for i in range(l):
    if s[i]==ch:
        print(i,end=" , ")