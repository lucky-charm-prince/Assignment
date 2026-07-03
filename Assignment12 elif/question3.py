transaction_amount=60000
location="domestic".lower()
account_age=1
otp="yes".lower()
activity="yes".lower()
if transaction_amount>=10000:
    if location=="international":
        if otp=="yes":
            print("allowed")
        else:
            print("blocked")
    else:
        if transaction_amount>=50000:
            if account_age>=2:
                print("allowes")
            else:
                print(" transaction=flag")
        else:
            print("allow")
else:
    if activity=="yes":
        print("transaction_satus=flag")
    else:
        print("allow")



    

