# S1 = "abc", S2 = "abc"  output :- TRUE
s1=input("String 1 : ")
s2=input("String 2 : ")
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        if s1[i]!=s2[i]:
            print("false ")
            break
    else:
        print("True")    
else:
    print("False")        


