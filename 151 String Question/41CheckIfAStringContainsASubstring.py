# S1 = "Hello", Sub="ell" output :- TRUE
s=input("String : ")
l1=len(s)
st=input("Str : ")
l2=len(st)

for i in range(0,l1-l2+1):
    if s[i:i+l2]==st:
        print("True")
        break
else:
    print("False")    