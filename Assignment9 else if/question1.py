age=int(input("enter the age="))
amount=int(input("enter the amount"))
type=input("enter the major type=").lower()
if age>=2:
    if amount<=50000:
        if type=="minor":
            print("approved claim")
        else:
            print("approve with inspection")
    elif amount>=50001 and amount<=200000:
        if type=="major":
            print("approved with investigation")
        else:
            print("reject")
    else:
        print("rejcet")
else:
    if type=="minor":
        print("reject")
    else:
        print("mark as a pending")
