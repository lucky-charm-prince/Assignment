# S1 = "listen", S2 = "silent" output:- TRUE

s1=input("String 1 : ")
s2=input("String 2 : ")
l1=len(s1)
l2=len(s2)
if l1==l2:
      for i in range(l1):
            c1=0
            c2=0
            for j in range(l2):
                  if s1[i]==s1[j]:
                        c1+=1
                  if s1[i]==s2[j]:
                        c2+=1
            if c1!=c2:
                  print("Not Anagram")            
                  break
      else:
            print("Anagram")      
else:
      print("Not Anagram")            

