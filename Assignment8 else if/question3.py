income=int(input("enter the annual income="))
if income<=250000:
    print("no tax")
elif income>=250001 and income<=500000:
    print((income*5)//100)
elif income>=500001 and income<=1000000:
    print((income*20)//100)
else:
    print((income*30)//100)