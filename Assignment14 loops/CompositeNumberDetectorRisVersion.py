# 6. Composite Number Detector – Risk Version

# A product company marks composite numbers as risky.

# User enters a number.
# System must:

# - Check Composite or Not
# - Count total factors
# - Print smallest factor other than 1

# Input:
# 12

# Output:
# Composite Number
# Factors Count = 6
# Smallest Factor = 2

n=int(input("Enter the number : "))
num=n
x=0
count=2
for i in range(2,n//2+1):
    if n%i==0:
        print("Number is compostie")
        x=1
        break
else:
   
        print("Numer is not composite")    

if x==1:
     for i in range(2,n//2+1):
        if n%i==0:  
          count+=1
     print("Total factor are : ",count)     