n=int(input("enter the number of rows="))
i=1
k=1
while i<=n:
    
    j=1
    while j<=i:
        print("*",end="")
        j+=1

    if i>2:
        x=1
        while x<=k:
            print("*",end="")
            x+=1    
        k*=3
    print()
    i+=1        

# *
# **
# ****
# *******
# ***********
