# 13. Employee Performance Appraisal System


# A company evaluates employees based on performance rating (1–5):

# * 5 → 25% salary hike
# * 4 → 20% salary hike
# * 3 → 10% salary hike
# * 2 → 5% salary hike
# * 1 → No hike
#   If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

# Write a Python program to calculate revised salary.

# Input:
# Enter salary: 18000
# Enter rating: 4

# Output:
# Revised Salary: ₹23600


salary=int(input("enter the salary="))
rating=int(input("enter the rating="))
if salary<20000:
    if rating>=4:
        print("revised slaary=",2000 +(salary)+(salary*20)//100)
    elif rating==3:
        print("revised salary=",(salary*10)//100)
    elif rating==2:
        print("revised salary=",(salary*5)//100)
    else:
        print("no hike")
else:
    print(" no anything")
  
