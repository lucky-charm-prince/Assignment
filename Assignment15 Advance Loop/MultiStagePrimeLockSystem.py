# 2. Multi Stage Prime Lock System


# A smart locker opens only if final derived number is prime.


# Write a program to:


# - Find sum of digits

# - Find product of digits

# - Find difference between product and sum

# - Count digits in difference

# - Add digit count to difference

# - Check whether final result is Prime or Not


# Input:

# 234


# Output:

# Sum = 9

# Product = 24

# Difference = 15

# Digits = 2

# Final Result = 17

# Prime




n=int(input("Enter the number : "))
sum=0
product=1
while n>0:
    x=n%10
    sum+=x
    product*=x
    n=n//10
diff=abs(product-sum)
print("Sum : ",sum)    
print("Product : ",product)    
print("Difference : ",diff)    
digit=len(str(diff))
print("Digits : ",digit)
finalReSult=diff+digit
print("Final Result : ",finalReSult)
for i in range(2,finalReSult//2+1):
    if finalReSult%i==0:
        print("NOt Prime")
        break
else:
    if finalReSult>1:
        print("Prime")    
    else:
        print("Not Prime")    

