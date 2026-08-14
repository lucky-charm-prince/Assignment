# 5.

# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and negative numbers
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input:
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input:
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0

# ----------------------------I am lazy so i take direct input isted of taking input form the user ----------------------

# n=int(input("Enter the size of array"))
# arr=[]
# for i in range(n):
#     arr.append(input("value"))
# print(arr)    

# arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
arr=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
pos=[]
neg=[]
for i in arr:
    if i >=0:
        pos.append(i)
    else:
        neg.append(i)
arr1=[]
x=0
while x<len(pos) and x<len(neg):
    arr1.append(pos[x])
    arr1.append(neg[x])
    x+=1
k=0    
y=0
if len(pos)>len(neg):
    k=len(pos)
    y=0
else:
    y=1
    k=len(neg)
while x<k:
    if y==0:
        arr1.append(pos[x])
    else:
        arr1.append(neg[x])
    x+=1
print(arr1)        
        

