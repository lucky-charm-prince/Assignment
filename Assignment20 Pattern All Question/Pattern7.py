# *
# **
# ****
# *******
# ***********



n=int(input("enter the number of rows="))

i=1
while i<=n:
    j=1
    while j<=n-i+1:
        if i+j==n+1 or j==1 or i==1:
            print("*",end="")
        else:
            print(" ",end="")    
        j+=1
    print()    
    i+=1        
