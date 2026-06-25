# 9. Check All Digits Are Even*
# A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
# Write a program to *check whether all digits of a number are even using loops*.

# Input: 2468
# Output: All Even

# Input: 2456
# Output: Not All Even



n = int(input("Enter the number : "))
count=0


# Using the for looopp
# for i in range(len(str(n))):
#     if ((n%10)%2)!=0:
#         count=1
#         break
#     n=n//10
# if count==1:
#     print("Not ALL Even ")    

# else:
#     print("ALL Even")       


while n>0:
    if ((n%10)%2)!=0:
        count=1
        break
    n=n//10
if count==1:
    print("Not ALL Even ")    

else:
    print("ALL Even")