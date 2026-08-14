# S1="CDAB", S2="ABCD" output:-  True (S1 is in S2+S2)

s1=input("String 1 : ")
s2=input("String 2 : ")
if s1  in s2+s2:
    print("True")
else:
    print("False")    