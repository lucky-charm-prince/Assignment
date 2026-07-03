demand=85
time="peak".lower()
distance=12
if demand>=80:
    if time=="peak":
        if distance>=10:
            print("apply 2x")
        else:
            print("aply1.5x")
    else:
        if demand>=90:
            print("1.8x")
        else:
            print("1.3x")
else:
    if demand>=50:
        print("peak time ")
        if time=="peak":
            print("apply 12x")
        else:
            print("normal fare")
    else:
        print("normal fare")
