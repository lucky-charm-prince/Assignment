distance=int(input("enter the distance="))
_class=input("enter the class =").lower()
if distance<=100:
    if _class=="sleeper":
        print("total fare=100")
    else:
        print("total fare=200")
elif distance>=101 and distance<=500:
    if _class=="sleeper":
        print("300")
    else:
        print("600")
else:
    if _class=="sleeper":
        print("500")
    else:
        print("1000")