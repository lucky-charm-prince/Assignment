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
