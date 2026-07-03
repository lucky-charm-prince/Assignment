
# 7.

#  Alternate Digit Prime Checker


# A math lab adds alternate digits from right side.


# Write a program to:


# - Find sum of alternate digits

# - Check whether sum is Prime or Not


# Input:

# 12345


# Output:

# Alternate Sum = 9

# Not Prime

n=int(input("Enter the numebr : "))
x=0

while n>0:
    x+=n%10
    n=n//100
    
    
alternateSum=x
print("AlternateSum",alternateSum)    

for i in range(2,alternateSum//2+1):
    if alternateSum%i==0:
        print("NOt Prime")
        break
else:
    if alternateSum>1:
        print("Prime")    
    else:
        print("Not Prime")    


