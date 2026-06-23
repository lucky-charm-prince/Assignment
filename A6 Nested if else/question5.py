balance=int(input("enter the balance="))
withdrawal_amount=int(input("enter the withdrawal amount="))
pin=input("enter the pin status correct or incorrect=").lower()
if balance>=withdrawal_amount:
    if withdrawal_amount<=10000:
        if pin=="correct":
            print("transaction succesfull")
        else:
            print("invalid pin")
    else:
        print("limit exceeded")
else:
    print("insufficient balance")