marks=int(input("enter the marks="))
backlogs=int(input("enter the backlogs="))
projects=int(input("enter the projects="))
if marks>=75:
    if backlogs==0:
        if projects>=80:
            print("first class with distinction")
        else:
            print("first class")
    else:
        print("first class")
elif marks>=60 and marks <=74:
    if backlogs<=2:
        print("assign second class ")
    else:
        print("pass class")
elif marks>50 and marks<=59:
    print("pass ")
else:
    print("fail")

