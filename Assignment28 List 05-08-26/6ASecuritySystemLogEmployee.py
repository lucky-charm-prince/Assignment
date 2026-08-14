# 6.

# A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.

# Tasks:

# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0
n=[12, 5, 7, 9, 11, 14, 17]
# n=[4, 6, 8, 10]
list=[]
sum=0
max=-1
count=0
for i in n:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        if i!=1 or 0:    
            count+=1
            sum+=i
            if i>max:
                max=i
            list.append(i)
print(list)
print(" Sum : ", sum) 
print(" Max : ",max )
print(" Count :",count)
