# 3. Smart Loan Risk Categorization

# A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

# If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.

# Input:
# Salary = 40000
# Credit Score = 760
# Existing Loans = 1

# Output:
# Risk Level = Medium Risk

salary=int(input("enter the salary="))
creadi_score=int(input("enter the salary="))
existing_lonas=int(input("enter the salary="))
if salary>=30000:
    if creadi_score>=750:
        if existing_lonas==0:
            print("low risk")
        elif existing_lonas<=2:
            print("medium risk")
        else:
            print("high risk")
    else:
        if salary>=50000:
            if creadi_score>=650:
                print("medium risk")
            else:
                print("high risk")
else:
    print("not eligible ")
