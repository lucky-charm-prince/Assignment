# 9. Student Attendance Eligibility System

# A college determines whether a student is eligible to sit for exams based on attendance percentage:

# * 75% and above → Eligible
# * 60% to 74% → Eligible with warning
# * Below 60% → Not eligible

# Write a Python program to check eligibility.

# Input:
# Enter attendance percentage: 58

# Output:
# Status: Not Eligible

attendance_per=int(input("enter the attendance percentage="))
if attendance_per>70:
    print("eligible")
elif attendance_per>=60 and attendance_per<=74:
    print("eligible with warning")
else:
    print("not eligible")