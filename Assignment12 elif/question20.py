age=int(input("enter the age="))
bmi=int(input("enter the bmi="))
running_time=int(input( "enter the time="))
medical=input("enter the medical type=").lower()
if age >18 and age<=25:
    if bmi>18 and age<=25:
        if running_time<=15:
            if medical=="fit":
                print("selcet")
            else:
                print("medical rejcet")
        else:
            print("physical fail ")
    else:
        print("bmi fail")
elif age >26 and age<30:
    if running_time<=14:
        if medical =="fit":
            print("conditional selection")
        else:
            print("rejcet")
else:
    if age>30 and age<18:
        print("not eligible")

