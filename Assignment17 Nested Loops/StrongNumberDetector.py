# 5.
# Strong Number Detector

# A banking security system uses Strong Numbers for special authentication testing.
# The user enters a range of numbers.
# The system identifies all Strong Numbers between the given range using nested loops.

# A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

# Example:
# 145

# 1! + 4! + 5!
# = 1 + 24 + 120
# = 145

# Since the sum is equal to the original number, 145 is called a Strong Number.

# Input:
# Enter starting number: 1
# Enter ending number: 500

# Output:
# Strong Numbers are:
# 1
# 2
# 145

x=int(input("Enter the number : "))
y=int(input("Enter the number : "))

for i in range(x,y+1):
    n=i
    sum=0

    while n>0:
        d=n%10
        k=1
        for j in range(1,d+1):
            k*=j
            
        sum+=k
        n=n//10

    
    if sum==i:
        print(i)        