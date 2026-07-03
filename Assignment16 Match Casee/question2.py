salary=0
while True:
    print("1 → Enter Basic Salary")
    print("2 → Calculate HRA (20%) and DA (10%)")
    print("3 → Calculate Net Salary")
    print("4 → Tax Deduction")
    print("5 → Display Salary Slip")
    print("6 → Exit")
    
    choice=int(input("enter the choice"))
    match choice:
        case 1:
            salary=int(input("enter the basic"))
            print("basic salary recoreded")
            
        case 2 :
            if salary==0:
                print("enter the basic salary")
            else:
                HRA=(salary*20)//100
                DA=(salary*10)//100
                print(HRA)
                print(DA)
        case 3:
            if salary==0:
                print("entered the basic salary first")
            else:
                net_salary=(((salary*20)//100)+((salary*10)//100))+salary
                print("net salary before tax",net_salary)
            
        case 4:
            if salary==0:
                print("enter the basic salary first")
            else:
                tax_deduction=net_salary=(((((salary*20)//100)+((salary*10)//100))+salary)*10)//100
                print(tax_deduction)
        case 5:
            if salary==0:
                print("the basic salary first")
            else:
                basic_salary=salary
                print(basic_salary)
                print("HRA=",(salary*20)//100)
                print("DA=",(salary*10)//100)
                print("net salary",(((salary*20)//100)+((salary*10)//100))+salary )
                print("tax",(((((salary*20)//100)+((salary*10)//100))+salary)*10)//100)
                print("final salary",46800)
        case 6:
            choice=int(input("enter the choice"))
            if choice==6:
                print("exiting program... Thank you")
                break
            else:
                print("invalid choice.please try again")

              
