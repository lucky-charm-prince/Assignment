#     #
#    *#* 
#   **#** 
#  ***#*** 
# ****#****


n=int(input("Enter the number : "))




# 11 12 13 14 15 16 17 18 19
# 21 22 23 24 25 26 27 28 29
# 31 32 33 34 35 36 37 38 39
# 41 42 43 44 45 46 47 48 49
# 51 52 53 54 55 56 57 58 59

i=1
while i<=n:
    j=1
    while j<=n*2-1:
        if i+j>=n+1 and j-i<=n-1:
            if n==j:
                print("#",end="")
            else:    
                print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1            

