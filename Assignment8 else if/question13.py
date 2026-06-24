salary=int(input("enter the salary="))
rating=int(input("enter the rating="))
if salary<20000:
    if rating>=4:
        print("revised slaary=",2000 +(salary)+(salary*20)//100)
    elif rating==3:
        print("revised salary=",(salary*10)//100)
    elif rating==2:
        print("revised salary=",(salary*5)//100)
    else:
        print("no hike")
else:
    print(" no anything")
  
