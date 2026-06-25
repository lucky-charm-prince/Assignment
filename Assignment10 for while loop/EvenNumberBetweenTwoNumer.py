# *10. Even Numbers Between Two Numbers*
# A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
# Write a program to *display all even numbers between two numbers using loops*.

# Input: 10, 20
# Output: 10 12 14 16 18 20


n1=int(input("Enter the  first number : "))
n2=int(input("Enter the  Second number : "))

if(n1%2!=0):
    n1+=1

# using the for loop

# for i in range(n1,n2+1,2):
#     print(i,end=" ")
    




while(n1<=n2):
    print(n1,end=" ")
    n1+=2
    


