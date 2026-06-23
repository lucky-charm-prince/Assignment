cart_value=int(input("enter the cart value="))
user_type=input("enter the user type=").lower()
if cart_value>=5000:
    if user_type=="premium":
        print((cart_value-(cart_value*20)/100 ))
    else:
        print((cart_value*10)/100)
else:
    if cart_value<=2000:
        print(print((cart_value*5)/100))       
    else:
        print("no discount is applied")