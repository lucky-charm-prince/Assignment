salary=int(input("enter the salary="))
credit_score=int(input("enter the credit score="))
existing_loans=int(input("enter the loans="))
if salary>=30000:
    if credit_score>=750:
        print("loan should be approved")
    else:
        if existing_loans<2:
            print("conditionaly approved")
        else:
            print("it should be rejected")
else:
    if salary<30000:
        print("the loan should be rejcted")