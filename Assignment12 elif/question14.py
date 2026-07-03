_class="economy".lower()
distance=1200
Booking="early".lower()
if _class=="business":
    if distance>=1000:
        print("8000")
    else:
        print("5000")
else: 
    if distance>1000:
        if Booking=="early":
            print(" trick = price is 4000")
        else:
            print("5000")
    else:
        print("2500")