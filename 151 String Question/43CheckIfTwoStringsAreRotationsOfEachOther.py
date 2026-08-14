# S1 = "abcde", S2 = "cdeab" output :- TRUE
s1=input("String 1 : ")
s2=input("String 2 : ")
if s1==s2:
    print("True")
else :
    if len(s1)==len(s2):
        s3=""    
        for i  in range(len(s1)):
            temp=s2[0:i]
            flag=s2[i:len(s1)]
            s3=flag+temp
            #print(s3)
            if s3==s1:
                print("True")
                break
        else:
            print("Flase")
    else:
        print("False")            


