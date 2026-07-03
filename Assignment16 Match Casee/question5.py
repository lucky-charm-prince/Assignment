unit=int(input("enter the units"))

if unit>=100:
    unit=unit-100
    value=100*5
    if unit>100:
        unit=unit-100
        value=value+100*7
        if unit>0:
            value=value+unit*10
            print("value =",value)
    else:
        value=value+unit*7
        print("value=",value)
else:
    value=unit*5
    print("the value",value)