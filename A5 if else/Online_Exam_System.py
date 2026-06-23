# 10. Online Exam System
#     System evaluates exam conditions:

# * If marks ≥ 40 → Pass
# * If attendance ≥ 75 → Eligible for certificate

# Input:
# Enter marks: 60
# Enter attendance: 80

# Output:
# Pass
# Eligible for certificate
marks=int(input("Enter the marks :"))
if marks>=40:
    print("Pass")
    attendance=int(input("Enter the attendence :"))
    if attendance>=75:
        print("Eligible for certificate")
    else:
        print("Not Eligible for certificate")
else:
    print("Fail")        