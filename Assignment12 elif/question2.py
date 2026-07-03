stock=120
priority="high".lower()
distance=300
if stock>=100:
    if priority=="high":
        if distance<=200:
            print("dispatch immediately")
        else:
            print("fast courier")
    else:
        if stock >=300:
            print("bulk dispatch ")
        else:
            print("normal dispatch")
else:
    if stock>=50:
        if priority=="high":
            print("partially dispatch")
        else:
            print("hold")
    else:
        print("out of stock")



