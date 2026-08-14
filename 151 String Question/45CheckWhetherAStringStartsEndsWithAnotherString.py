s=input("String : ")
l=len(s)
pre=input("Prefix : ")
l1=len(pre)
suf=input("Suffix : ")
l2=len(suf)

if l>=l1:
    if s[0:l1]==pre:
        print("Prefix : True")
    else:
        print("Prefix : False")    
if l>=l2:
    if s[l-l2:l]==suf:
        print("Suffix : True")        
    else:
        print("Suffix : False")    