units=int(input("enter the units consumed="))
total=0
if units>=100:
    total=100*5
    units=units-100
    if units>=100:
        total=total+(100*7)
        units=units-100
        print("total elcecticity bill=",total)
        if units>0:
            total=total+(units*10)
            print("total elcecticity bill=",total)
    else:
        total=total+units*7
else:
    total=units*5
    print("total elcecticity bill=",total)
