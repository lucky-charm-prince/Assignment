# S = "aabcc" a: 2, b: 1, c: 2


s=input("String : ")
 
s1=""
for i in s:
    if i not in s1:
        s1+=i
        count=0
        for j in s:
          if i==j:
            count+=1
        print(i," : ",count,end=" , ")    


