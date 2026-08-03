#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1

# 11 12 13 14 15 16 17 18 19
# 21 22 23 24 25 26 27 28 29
# 31 32 33 34 35 36 37 38 39
# 41 42 43 44 45 46 47 48 49
# 51 52 53 54 55 56 57 58 59
# 61 62 63 64 65 66 67 68 69
# 71 72 73 74 75 76 77 78 79
# 81 82 83 84 85 86 87 88 89
# 91 92 93 94 95 96 97 98 99

n=int(input("Enter the numbner : "))
i=1
x=1
while i<=n*2-1:
    j=1
    y=1
    while j<=n*2-1:

        if j==n and i<n:
            print(x,end="")
            x+=1
        elif j==n and i>=n:
            
            print(x,end="")
            x-=1
        elif i==n and j<=n:
            print(y,end="")       
            y+=1
        elif i==n and j>n:
            y-=1
            print(y,end="")    
        else:
            print(" ",end="")  
        j+=1
    i+=1
    print()          
