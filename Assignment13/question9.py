no=int(input("enter the no="))
t1=0
t2=0
sum=0
larg=0
for i in range(len(str(no))):
    t1=no%10
    no=no//10
    if no==0:
        break
    t2=no%10
    diff=abs(t1-t2)
    sum=(sum+diff)
print(diff,end=" ",)
print(" The sum=",sum)