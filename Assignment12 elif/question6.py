experience=6
rating=4
projects=2
salary=int(input("enter the salary="))
if experience>5:
    if rating>=4:
        if projects>=3:
            if salary<=50000:
                print("promote with 30 percent hike")
            else:
                print("10 percent hike")
        else:
            print("promote with 10 percent hike")
    else:
        print("no promotion")
else:
    if rating==5:
        print("fast track promotion")
    else:
        print("no promotion")
    
