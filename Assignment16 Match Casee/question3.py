deposit=0
while True:
    print("1.deposit money")
    print("2.withdraw money")
    print("3.check balance")
    print("4.apply interest")
    print("5.exit")
    
    choice=int(input("enter the choice"))
    match choice:
        case 1:
            deposit=int(input("enter the deposit amount"))
            print("amount deposited successfully")
        case 2:
            if deposit==0:
                print("no balance available.please deposit first")
            else:
                witdh=int(input("enter the withdrawl amount"))
                if witdh<=deposit:
                    print(deposit-witdh)
                    print("withdrwal succefull")
                else:
                    print("insufficient balance")
        case 3:
            if deposit==0:
                print("no balance available.please deposit first")
            else:
                current=deposit
                print("the current amount",current)
        case 4:
            if deposit==0:
                print("no balance available.please deposit first")
            else:
                if current>50000:
                    interest=((current*5)//100)
                    update=interest+current
                    print("interest added",interest)
                    print("update balance",update)
                else:
                    interest=((current*3)//100)
                    update=interest+current
                    print("interest added",interest)
                    print("update balance",update)
        case 5: 
            choice=int(input("enter the choice"))
            if choice==5:
                print("exiting system...Thank you!")
                break
            else:
                print("invalid choie.please try again")
            
                