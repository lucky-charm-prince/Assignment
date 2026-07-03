marks=88
income=250000
category="obc".lower()
if marks>85:
    if income<=300000:
        if category!="genral":
            print("full scholarship")
        else:
            print("give 75% scholarship")
    else:
        print("50% scholarship")
elif marks>=70 and marks<=84:
    if income<=200000:
        print("50% scholarship")
    else:
        print("25 % scholarship")
else:
    print("no scholarship")