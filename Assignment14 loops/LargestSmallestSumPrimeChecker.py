# 8. Largest Smallest Sum Prime Checker

# A number analyzer finds largest and smallest digit.

# Write a program to:

# - Find largest digit
# - Find smallest digit
# - Find sum of both
# - Check whether sum is Prime or Not

# Input:
# 57294

# Output:
# Largest = 9
# Smallest = 2
# Sum = 11
# Prime

n=int(input("Enter the number : "))
largest=0
smallest=9
sum=0
while n>0:
    temp=n%10
    if largest<temp:
        largest=temp
    if smallest>temp:
        smallest=temp
    n=n//10

print("Largest : ",largest)
print("Smallest : ",smallest)
sum=largest+smallest
print("Sum : ",sum)
for i in range(2,sum//2+1):
    if sum%i==0:
        print("not Prime")           
        break
else:
    if sum>1:
        print("Pime")     
    else:
        print("Not prime")    