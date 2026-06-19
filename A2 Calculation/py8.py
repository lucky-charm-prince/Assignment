#Print the simple interst 

principle,rate,time=map(int,input("Enter the amount, rate,time ").split(","))
si=float(principle*rate*time/100)
print("Simple Interest: ",si)
