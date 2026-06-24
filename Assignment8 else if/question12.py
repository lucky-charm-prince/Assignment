bill_amount=int(input("enter the bill amount="))
if bill_amount<=1000:
    print("final bill amount=",bill_amount+(bill_amount*5)//100)
elif bill_amount>=1001 and bill_amount<=5000:
    print("final bill amount=",200+(bill_amount+(bill_amount*12)//100))
else:
    print("final bill amount=",bill_amount+(bill_amount*18)//100)