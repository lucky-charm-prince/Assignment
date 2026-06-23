unit_1=int(input("enter the units="))
unit_2=int(input("enter the units="))
unit_3=int(input("enter the units="))
unit_4=int(input("enter the units="))
unit_5=int(input("enter the units="))
unit_6=int(input("enter the units="))
if unit_1>unit_2:
    if unit_1>unit_3:
        if unit_1>unit_4:
            if unit_1>unit_5:
                if unit_1>unit_6:
                    print("hishest Stock is ",unit_1)
                else:
                    print("the highest stock =",unit_6)
            else:
                if unit_5>unit_6:
                    print("highest stock=",unit_5)
                else:
                    print("higest stock =",unit_6)
        else:
            if unit_4>unit_5:
                print("higest stock =",unit_4)
            else:
                print("higest stock =",unit_5)
    else:
        if unit_3>unit_4:
            print("higest stock =",unit_3)
        else:
            print("higest stock =",unit_4)
else:
    if unit_2>unit_3:
        if unit_2>unit_4:
            if unit_2>unit_5:
                if unit_2>unit_6:
                    print("highest stock is ",unit_2)
                else:
                    print("higest stock =",unit_6)
            else:
                if unit_5>unit_6:
                    print("higest stock =",unit_5)
                else:
                    print("higest stock =",unit_6)
        else:
            if unit_4>unit_5:
                print("higest stock =",unit_4)
            else:
                print("higest stock =",unit_5)
    else:
        if unit_3>unit_4:
            print("higest stock =",unit_3)
        else:print("higest stock =",unit_4)


            