# A
# BCD
# EFGHI
# JKLMNOP


n=int(input("Enter the number : "))

i=1
x=65
while i<=n:
    j=1
    while j<=i*2-1:
        print(chr(x),end="")
        x+=1
        j+=1
    i+=1    
    print()
