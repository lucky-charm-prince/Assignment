order_amount=2500
customer_type="vip".lower()
payment_="online".lower()
if order_amount>=2000:
    if customer_type=="vip":
        if payment_=="online":
            print("free desert and 20% discount")
        else:
            print("free desert")
    else:
        if order_amount>=5000:
            print("15 percent discount")
        else:
            print("10% discount")
else:
    if order_amount<=1000:
        if customer_type=="vip":
            print("10% discount")
        else:
            print("5 percent discount")
    else:
        print("no offer")