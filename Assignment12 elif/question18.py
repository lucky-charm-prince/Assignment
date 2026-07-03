demand=int(input("enter the no ="))
stock=int(input("enter the no ="))
user_type=input("enter the type=").lower()
festival=input("enter the festival=").lower()
if demand>=80:
    if stock<50:
        if user_type=="premium":
            if festival=="yes":
                print("20% discount ")
            else:
                print("10% discount")
        else:
            print("no discount")
    else:
        print("give 5 % ")
else:
    if stock >=200:
        print("15% discount ")
    else:
        print("no discount")
