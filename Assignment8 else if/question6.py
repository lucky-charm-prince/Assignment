salary=int(input("enter the salary="))
experience=int(input("enter the experience"))
if experience>10:
    print("bonus amount=",(salary*20)//100)
elif experience>=5 and experience<=10:
    print("bonus amount=",(salary*10)//100)
elif experience>=2 and experience<=5:
    print("bonus amount=",(salary*5)//100)
else:
    print("no bouns")