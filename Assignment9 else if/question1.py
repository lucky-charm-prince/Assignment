# 1. Insurance Claim Approval System

# An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

# If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

# Input:
# Policy Age = 3
# Claim Amount = 120000
# Accident Type = major

# Output:
# Claim Status = Approved with Investigation


age=int(input("enter the age="))
amount=int(input("enter the amount"))
type=input("enter the major type=").lower()
if age>=2:
    if amount<=50000:
        if type=="minor":
            print("approved claim")
        else:
            print("approve with inspection")
    elif amount>=50001 and amount<=200000:
        if type=="major":
            print("approved with investigation")
        else:
            print("reject")
    else:
        print("rejcet")
else:
    if type=="minor":
        print("reject")
    else:
        print("mark as a pending")
