# 9.Even Odd Difference Prime System

# A smart scanner counts even and odd digits.

# Write a program to:

# - Count even digits
# - Count odd digits
# - Find difference
# - Check whether difference is Prime or Not

# Input:
# 123456

# Output:
# Even Count = 3
# Odd Count = 3
# Difference = 0
# Not Prime

n=int(input("Enter the number : "))

count_Odd=0
count_Even=0
Diff=0

while n>0:
    x=n%10
    if x%2==0:
        count_Even+=1
    else:
        count_Odd+=1
    n=n//10    
print("Even is ",count_Even)
print("Odd is ",count_Odd)
Diff=abs(count_Even-count_Odd)
flag=0

for i in range(2,Diff//2):
    if Diff%i==0:
        flag=1
        break
else:
    if Diff>0:
        print("Differnce is Prime ",Diff)    
    else:    
        print("Differnce is not Prime ",Diff) 
if flag==1:
      print("Differnce is not Prime ",Diff)       