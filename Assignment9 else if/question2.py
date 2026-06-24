marks=int(input("enter the marks="))
score=int(input("enter the score="))
category=input("enter the category").lower()
if marks>=70:
    if score >=80:
        if category=="general":
            print("admited")
        else:
            print("admit with scholarship")
    else:
        if marks>=85:
            print("admit under management quota")
        else:
            print("reject")
else:
    if category!= "genral" and marks>=60:
        if score >=70 :
            print("waitlist")
        else:
            print("reject")
    else:
        print("reject")

