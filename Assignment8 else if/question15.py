vehicle=input("enter the vehicle type=").lower()
hours=int(input("enter the hours="))
if vehicle=="bike":
    if hours>5:
        print("total parking=",(hours*10)+100)
    else:
        print("total parking=",(hours*10))
elif vehicle=="car":
    if hours>5:
        print("total parking=",(hours*20)+100)
    else:
        print("total parking=",(hours*20))
elif vehicle=="bus":
    if hours>5:
        print("total parking=",(hours*50)+100)
    else:
        print("total parking=",(hours*50))