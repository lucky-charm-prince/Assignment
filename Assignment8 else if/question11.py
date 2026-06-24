# 11. Railway Ticket Fare System


# A railway system calculates ticket fare based on distance and travel class:

# * Distance ≤100 km:
#   Sleeper → ₹100, AC → ₹200
# * Distance 101–500 km:
#   Sleeper → ₹300, AC → ₹600
# * Distance >500 km:
#   Sleeper → ₹500, AC → ₹1000

# Write a Python program to calculate ticket fare.

# Input:
# Enter distance: 350
# Enter class: AC

# Output:
# Total Fare: ₹600

distance=int(input("enter the distance="))
_class=input("enter the class =").lower()
if distance<=100:
    if _class=="sleeper":
        print("total fare=100")
    else:
        print("total fare=200")
elif distance>=101 and distance<=500:
    if _class=="sleeper":
        print("300")
    else:
        print("600")
else:
    if _class=="sleeper":
        print("500")
    else:
        print("1000")