purchase_amount=int (input("enter the purchase amount="))
if purchase_amount>5000:
    print("Final Amount=", purchase_amount-(purchase_amount*20)//100)
elif purchase_amount>=2000 and purchase_amount<=5000:
    print("Final Amount=",purchase_amount-(purchase_amount*10)//100)
else:
    print("Final Amount=",purchase_amount-(purchase_amount*5)//100)