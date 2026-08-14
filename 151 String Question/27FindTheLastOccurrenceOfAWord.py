# S = "Test this test", Word = "test"   output :- 15 (index)
s=input("String : ")

l1=len(s)
word=input("word : ")
l2=len(word)
start=0
x=-1
for i in range(0,l1):
    if s[i]==' ':
        if i-start==l2 and word==s[start:i]:
            x=start
            
        start=i+1
else:
    k=0
    if l1-start==l2 and word==s[start:]:
       
        x=start
        print(x)
        k+=1
    else:
        if k==0:
            print(x)   
           
        else:
            print("not found")           
            
        