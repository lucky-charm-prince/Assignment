amount=70000
location="international".lower()
device="new".lower()
transactions=4
if amount>=50000:
    if location=="international":
        if device=="new":
            if transactions>3:
                print("mark high rishk(block)")
            else:
                print("medium risk")
        else:
            print("medium risk")
    else:
        if transactions>5:
            print("mark medium risk")
        else:
            print("low risk")
else:
    if input("enter activity=")=="unusal":
        if device=="new":
            print("mark medium risk ")
        else:
            print("low risk")
    else:
        print("marks safe")
