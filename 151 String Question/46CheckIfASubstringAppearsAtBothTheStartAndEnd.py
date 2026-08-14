# S = "abcabca", Sub="abca" output :- TRUE

s=input("String : ")
l=len(s)

sub=input("SubString : ")
l1=len(sub)

if l>=l1 and s[0:l1]==sub and s[l-l1:l]==sub:
    print("true")
else:
    print("false")    
    