# 10.Zero Count Prime Scanner

# A banking system checks account numbers.

# Write a program to:

# - Count zero digits
# - Find sum of digits
# - Add zero count and sum
# - Multiply by smallest digit
# - Check whether final result is Prime or Not

# Input:
# 908406

# Output:
# Zero Count = 2
# Sum = 27
# Smallest Digit = 0
# Final Result = 0
# Not Prime

num=int(input("Enter the number : "))
n=num
zeroCount=0
sum=0
smallestDigit=9
finalResult=0

while n>0:
    x=n%10
    sum+=x
    if x==0:
        zeroCount+=1
    if smallestDigit>x:
        smallestDigit=x
    n=n//10    

print("zero count ",zeroCount)
print("Digit sum : ",sum)
print("Smallest digit : ",smallestDigit)
finanlResult=sum*smallestDigit
for i in range(2,((finalResult//2)+1)):
    if num%i==0:
        print("Not prime",finalResult)
        break
else:
    if finalResult==0 or finalResult==1 :
        print("not Prime ",finalResult)
    else:    
      print("prime",finalResult)    
      