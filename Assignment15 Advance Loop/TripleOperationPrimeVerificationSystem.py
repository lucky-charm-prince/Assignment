# 1. Triple Operation Prime Verification System


# A cybersecurity company generates a security score from entered access code.


# Write a program to:


# - Find sum of digits of the number

# - Reverse the number

# - Find absolute difference between original number and reverse

# - Add digit sum and difference

# - Check whether final result is Prime or Not Prime


# Input:

# 4215


# Output:

# Sum of Digits = 12

# Reverse = 5124

# Difference = 909

# Final Result = 921

# Not Prime

from typing import final


n=int(input("Enter the number : "))
n1=n
sum=0
temp=0

while n>0:
    x=n%10
    temp=temp*10+x
    sum+=x
    n=n//10

print("Sum of digit : ",sum)
print("Reverse = ",temp)
diff=abs(temp-n1)
print("Difference : ",diff)
finalReSult=diff+sum
print("FinalResult : ",finalReSult)
for i in range(2,finalReSult//2+1):
    if finalReSult%i==0:
        print("NOt Prime")
        break
else:
    if finalReSult>1:
        print("Prime")    
    else:
        print("Not Prime")    
