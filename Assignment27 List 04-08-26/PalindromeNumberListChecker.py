# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]

n=list(map(int,input("Enter the list : ").split()))
largest=0
count=0
new=[]
for i in n:
    x=i
    k=0
    while i>0:
        k=k*10+i%10
        i=i//10
    if k==x:
        new.append(k)
        count+=1
        if k>largest:
            largest=k
print(new)
print(count)
print(largest)
new.sort()
print(new)            
