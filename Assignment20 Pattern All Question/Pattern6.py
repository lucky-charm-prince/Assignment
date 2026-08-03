# 123456
# 54321
# 1234
# 321
# 12
# 1



n=int(input("enter the number of rows="))

i=1
while i<=n:
    j=1
    x=1
    k=n-i+1
    while j<=n-i+1:
        if i%2!=0:
            print(x,end="")
            
        else:
            print(k,end="")    
        j+=1
        x+=1
        k-=1
    print()    
    i+=1        
