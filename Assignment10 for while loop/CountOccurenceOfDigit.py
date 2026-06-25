# *11. Count Occurrence of a Digit*
# A system logs repeated digits in a number for pattern analysis and reporting.
# Write a program to *count how many times a given digit appears in a number using loops*.

# Input: Number = 122312, Digit = 2
# Output: 3

n=int(input("Enter the number : "))
digit=int(input("Enter the digit : "))
count=0


# for i in range(len(str(n))):
#     if(n%10==digit):
#         count+=1
#     n=n//10

# print(digit ,"Occurence : ",count)


while(n>0):
    if(n%10==digit):
        count+=1
    n=n//10

print(digit ,"Occurence : ",count)