stock=int(input("ennterthe stock"))
prority = input("the the prioprity=").lower()
distance=int(input("enter the distance="))
if stock >=100 :
    if prority=="high":
        if distance<=200:
            print("dispatch immediatly")
        else:
            print("fast courier")
    else:
        if stock>=300:
            print("bulk dispatc")
        else:
            print("normal dispatch ")
else:
    if stock>=50:
        if prority=="high":
            print("partially dispatch ")
        else:
            print("hold")
    else:
        print("out of stock")