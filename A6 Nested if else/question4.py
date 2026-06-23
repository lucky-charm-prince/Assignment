age=int(input("enter the age="))
weight=int(input("enter the weight="))
goal=input("enter the goal=").lower()
if age>=18:
    if weight>=80:
        if goal=="weight loss":
            print("cardio plan")
        else:
            print("strength plan")
    else:
        print("genral fitness plan")
else:
    print("not allowed ")