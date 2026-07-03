salary=int(input("enter the salary="))
age=int(input("enter the age="))
credit_score=int(input("enter the no="))
emi=int(input("enter the emi="))
if salary>=40000:
    if age>21 and age<=60:
        if credit_score>750:
            if emi<=(salary*40)/100:
                print("the approve at 8%")
            else:
                print(" approve10 %")
        else:
            if credit_score>=650:
                print("approve at 12%")
            else:
                print("reject")
else:
    if salary<40000:
        if salary>=25000:
            if credit_score>=700:
                print("approve")
            else:
                print("rejct")

