category=input("enter the course name=").lower()
user_type=input("entter the type=").lower()
if category=="programming":
    category=5000
    if user_type=="student":
        print("final course fee=",category-(category*20)//100)
    elif user_type=="working":
        print("final course fee=",category-(category*10)//10)
    else:
        print("no discount")

elif category=="desing":
    category=4000
    if user_type=="student":
        print("final course fee=",category-(category*20)//100)
    elif user_type=="working":
        print("final course fee=",category-(category*10)//10)
    else:
        print("no discount")
elif category=="marketing":
    category=3000
    if user_type=="student":
        print("final course fee=",category-(category*20)//100)
    elif user_type=="working":
        print("final course fee=",category-(category*10)//10)
    else:
        print("no discount")
else:
    print("enter the valid name")

