balance=int(input("enter the balance="))
if balance<1000:
    print("withdrawal not allowed")
elif balance>=1000 and balance<=5000:
    print("maximum withdrawal limit=1000")
else:
    print("maximum withdrawal limit= 5000")
