experience=int(input("enter the experience="))
rating=int(input("enter the rating="))
salary=int(input("enter the salary="))
if experience>=5:
    if rating>=4:
        if salary<=50000:
            print((salary*20)//100)
        else:
            print((salary*10)//100)
    else:
        print((salary*5)//100)
else:
    print("no bonus is given")
