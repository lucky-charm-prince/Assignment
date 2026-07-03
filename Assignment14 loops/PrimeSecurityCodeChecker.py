# 1. Prime Security Code Checker

# A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
#  only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

# When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

# Write a program to check whether the entered number is Prime or Not Prime.

# Input:
# 29

# Output:
# Prime Number

n=int(input("Enter the number : "))
flag=0
for i in range(2,n//2):
    if n%i==0:
        flag=1
        break
else:
    if n>0:
        print("Prime Number")    
    else:
        print("Not Prime")
if flag==1:
    print("Not prime")            