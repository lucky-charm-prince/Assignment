soil_moisture=25
temp=36
crop="high".lower()
rainfall="expected"
if soil_moisture<30:
    if temp>=35:
        if crop=="high":
            print("water supply")
        else:
            print("moderate supply")
    else:
        print("moderate supply")
else:
    if soil_moisture<=60:
        if rainfall=="expected":
            print("daily irrigation")
        else:
            print("light irrrigation ")
    print("irrigation")

