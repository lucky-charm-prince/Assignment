# 7.
#  Prime Sum Lucky Number

# A lottery app checks if sum of digits is prime.

# Write a program to:

# - Find sum of digits
# - If prime print Lucky Number
# - Else Normal Number

# Input:
# 4528

# Output:
# Sum = 19
# Lucky Number

n=int(input("Enter the number : "))

sum=0
while n>0:
    temp=n%10
    sum+=temp
    n=n//10
print("Sum : ",sum)    
for i in range(2,sum//2+1):
    if sum%i==0:
        print("Normal number")
        break
else:
    print("Lucky number")    
