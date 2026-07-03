unit=0
while True:
    print("1.enter units consumed")
    print("2.enter bill amount")
    print("3.apply surcharge ")
    print("4.display final bill")
    print("exit")
    
    choice=int(input("enter the choice") 
    match choice:
    case 1:
        unit=input("enter the units consumed")
        print("units recorded successfully")
    case 2:
        if unit==0:
            print("please enter units consumed first")
        else:
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
    case 3:
        if unit==0:
            print("please enter units consumed first")
        else:
            if value>2000:
                surcharge=value*0.1
                print("surcharge:",surcharge)
            else: 
                surcharge=value*0.05
                print("surcharge:",surcharge)
            
    case 4:
         if unit==0:
         print("please enter units consumed first")
         else:
             units=unit
             print("the units is=",units)
             bill_amount=value
             print("bill amount",bill_amount)
             surcharge=surcharge
             print("surcharge",surcharge)
             total=bil_amount+surcharge
             print("total=",total)
    case 5:
         if choice==5:
             print("exiting system...Thank you)
             break
         else:
             print("invalid choice")
 

      