# 12. Multiplication of Digits*
# A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
# Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.



n= int(input("Enter the number : "))
total=0
if n>0:
    
    total=1


#For loop
# for i in range(len(str(n))):
#       total*=n%10
#       n=n//10
# if total%2==0:
#     print(total)
#     print(" even")    
# else :
#     print("Odd")


while n>0:
      total*=n%10
      n=n//10
if total%2==0:
    print(total)
    print(" even")    
else :
    print("Odd")
        
        