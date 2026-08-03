# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    while j<=n*2:
        if i+j<=n+1 or j-i>n-1:
            print("*",end="")
        else:
            print(" ",end="")    
        j+=1
    i+=1
    print()        

i=1
while i<=n:
    j=1
    while j<=n*2:
        if j<=i or i+j>n*2:
            print("*",end="")
        else:
            print(" ",end="")    
        j+=1
    i+=1
    print()            