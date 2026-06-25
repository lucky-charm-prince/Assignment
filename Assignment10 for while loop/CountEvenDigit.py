# *7. Count Even Digits*
# A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
# Write a program to *count the number of even digits in a given number using loops*.

# Input: 123456
# Output: Even digits count = 3

n = int(input("Enter the number : "))
count=0


# Using the for looopp
# for i in range(len(str(n))):
#     if ((n%10)%2)==0:
#         count+=1
#     n=n//10
# print("Even digit is ",count)        


while n>0:
    if ((n%10)%2)==0:
        count+=1
    n=n//10
print("Even digit is ",count)        