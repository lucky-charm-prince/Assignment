# 4.Unique Digit Security Scanner


# A smart locker accepts only numbers whose all digits are unique.


# Write a program using for-else loop to:


# - Check every digit

# - If any repeated digit found reject

# - Else accept


# Input:

# 57294


# Output:

# Valid Unique Code

# n=int(input("Enter the number : "))
# oneDigit=0
# twoDigit=0
# threeDigit=0
# fourDigit=0
# fiveDigit=0
# sixDigit=0
# sevenDigit=0
# eightDigit=0
# nineDigit=0
# zeroDigit=0
# temp=n

# while n>0:
#     x=n%10
#     if x==1:
#         oneDigit+=1
#     elif x==2:
#         twoDigit+=1
#     elif x==3:
#         threeDigit+=1
#     elif x==4:
#         fourDigit+=1
#     elif x==5:
#         fiveDigit+=1
#     elif x==6:
#         sixDigit+=1
#     elif x==7:
#         sevenDigit+=1
#     elif x==8:
#         eightDigit+=1
#     elif x==9:
#         nineDigit+=1
#     else:
#         zeroDigit+=1
#     n=n//10
#     if oneDigit>1 or twoDigit>1 or threeDigit>1 or fourDigit>1 or fiveDigit>1 or sixDigit>1 or sevenDigit>1 or eightDigit>1 or nineDigit>1 or zeroDigit>1:
#         print("Invalid Code")
#         break
# else:
#     print("Valid Unique Code")    


n=int(input("Enter the number : "))
temp=n
k=0
while temp>0:
    x=temp%10
    temp=temp//10
    z=temp
    while z>0:
        y=z%10
        
        if x==y:
            
            k=1
            break
        z=z//10
    
    
        

else:
     if k==1:
         print("Invalid")
     else:
         print("Valid")
         
