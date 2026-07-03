# 7.
# Neon Number Detector

# Scenario:
# A smart calculator system checks special numbers used in mathematical testing.
# The user enters a range of numbers.
# The system identifies all Neon Numbers using nested loops.

# Theory:
# A Neon Number is a number where the sum of digits of its square is equal to the original number.

# Example:
# 9

# Square of 9 = 81

# 8 + 1 = 9

# Since the sum is equal to the original number, 9 is called a Neon Number.

# Input:
# Enter starting number: 1
# Enter ending number: 100

# Output:
# Neon Numbers are:
# 1
# 9

x=int(input("Enter the number : "))
y=int(input("Enter the number : "))

for i in range(x,y+1):
    sum=0
    sqr=i**2
    n=sqr
    
    while n>0:
        d=n%10
        sum+=d
        n=n//10
    
    
    if sum==i:
        print(sum)    
