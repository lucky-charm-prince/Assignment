# 4.
# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.


#   -------------------------------I am lazy so i take direct input insted of taking input from the user 
# n=int(input("Enter the size of the array1"))
# A=[]
# for i in range(n):
#     x=int(input("value : "))
#     A.append(x)
# n=int(input("Enter the size of the array2"))
# B=[]
# for i in range(n):
#     x=int(input("value : "))
#     B.append(x)

# n=int(input("Enter the size of the array3"))
# C=[]
# for i in range(n):
#     x=int(input("value : "))
#     C.append(x)
     
A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
for i in range(len(A)):
    x=0
    for j in range(len(B)):
        if A[i]==B[j]:
            x+=1
    y=0        
    for j in range(len(C)):
        if A[i]==C[j]:
            y+=1
    if y!=0 and x!=0:
        print(A[i])



