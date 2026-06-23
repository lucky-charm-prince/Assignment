# 4. Gym Membership Eligibility Checker
#    A gym checks multiple conditions:

# * If age ≥ 18 → Allowed for gym
# * If BMI > 25 → Suggest weight loss program

# Input:
# Enter age: 25
# Enter BMI: 27

# Output:
# Gym access granted
# Enroll in weight loss program

age=int(input("Enter the age"))
if age>=18:
    print("Gym access granted")
    bmi=int(input("Enter the bmi"))
    if bmi>25:
        print("Enroll in weight loss program")
    else:
        print("Not Enroll for the weight loss program")    
else:
    print("Gym access not granted")        