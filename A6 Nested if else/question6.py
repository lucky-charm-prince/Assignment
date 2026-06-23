age=int(input("enter the age="))
show_time=input("enter the show time morning/evening=").lower()
day=input("enter the day weekday/weekend =")
if age<=18:
    if show_time=="morning":
        print("ticket price is 100")
    else:
        print("ticket price is 150")
else:
    if show_time=="evening":
        if day =="weekend":
            print("ticket price is 300")
        else:
            print("ticket price is 250")
    else:
        print("ticket price is =200")
    