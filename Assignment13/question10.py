no=int(input("enter the no="))
"""
for i in range(2,no//2):
    if no%i==0:
        print("not prime no")
        break

else:
    print("the prime NO")"""
x=0
if no<=1:
   print("no prime NO")
else:
    i=2
    while i<no:
        if no%i==0:
            x=1
        i=i+1
    if x==0:
        print("prime")
    else:
        print("not prime")