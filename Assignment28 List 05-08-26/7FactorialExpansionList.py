# 7.
# Factory Production – Factorial Expansion List

# Problem Statement

# A factory produces items where production capacity is defined using factorial growth.

# Given a list of numbers, replace each number with its factorial value.

# Then perform analysis on the resulting list.

# Tasks:

# Convert each element to factorial
# Find sum of all factorial values
# Find maximum factorial value
# Count how many factorial values are even

# Input:
# A list of integers

# Example 1

# Input:
# [3, 4, 5]

# Processing:
# 3! = 6
# 4! = 24
# 5! = 120

# Output:
# [6, 24, 120]
# Sum = 150
# Max = 120
# Even Count = 3


n=[3, 4, 5]
sum=0
max=0
count=0
list=[]
for i in n:
    
    k=1
    while i>0:
        k*=i
        i-=1
    list.append(k)
    if k%2==0:
        count+=1
    sum+=k
    if k>max:
        max=k    

print(list)        
print("sum : ",sum)        
print("max : ",max)        
print("count : ",count)        