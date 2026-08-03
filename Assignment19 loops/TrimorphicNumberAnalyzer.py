# 8.
# Trimorphic Number Analyzer

# A coding system checks cube-based patterns.

# A Trimorphic Number:
# Cube of number ends with the same number.

# Example:
# 4³ = 64

# Write a program to check Trimorphic Number.

# Input:
# 4

# Output:
# Trimorphic Number

n=int(input("Enter the number "))

x=n**3
k=0
while n>0:
    a=x%10
    b=n%10
    if a!=b:
        k=1
        break
    x=x//10
    n=n//10
else:
    print("Trimorphic number")    
if k==1:
    print("Not Trimorphic Number")    