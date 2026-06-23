units=int(input("enter the units="))
if units>=100:
    if units>=300:
        print("high usage")
    else:
        if units>=200:
            print(" usage categroy=moderat eusage")
        else:
            print("normal usage")
else:
    print("low usage")