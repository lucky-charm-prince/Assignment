# 14. Online Course Fee System

# An online platform offers courses with fixed fees:

# * Programming → ₹5000
# * Design → ₹4000
# * Marketing → ₹3000
#   Discount is applied based on user type:
# * Student → 20% discount
# * Working Professional → 10% discount
# * Others → No discount

# Write a Python program to calculate final course fee.

# Input:
# Enter course category: Programming
# Enter user type: Student

# Output:
# Final Course Fee: ₹4000


category=input("enter the course name=").lower()
user_type=input("entter the type=").lower()
if category=="programming":
    category=5000
    if user_type=="student":
        print("final course fee=",category-(category*20)//100)
    elif user_type=="working":
        print("final course fee=",category-(category*10)//10)
    else:
        print("no discount")

elif category=="desing":
    category=4000
    if user_type=="student":
        print("final course fee=",category-(category*20)//100)
    elif user_type=="working":
        print("final course fee=",category-(category*10)//10)
    else:
        print("no discount")
elif category=="marketing":
    category=3000
    if user_type=="student":
        print("final course fee=",category-(category*20)//100)
    elif user_type=="working":
        print("final course fee=",category-(category*10)//10)
    else:
        print("no discount")
else:
    print("enter the valid name")

