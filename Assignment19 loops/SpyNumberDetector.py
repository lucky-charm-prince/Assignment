# 4.Spy Number Detector

# A cybersecurity system flags special numeric codes.

# A number is called a Spy Number if:
# Sum of digits = Product of digits

# Write a program to check whether the entered number is Spy Number or Not.

# Input:
# 1124

# Output:
# Spy Number

n=int(input("Enter the number : "))
total=0
multi=0

if n>0:
    multi=1

while n>0:
    d=n%10
    total+=d
    multi*=d
    n=n//10
if total==multi:
    print("Spy number")    
else:
    print("Not a spy number")    