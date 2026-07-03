income=45000
credit_score=720
employment="private"
debt=10000
if income>=50000:
    if credit_score>=750:
        if debt<20000:
            print("approve premium card")
        else:
            print("gold card")
    else:
        if employment=="government":
            if credit_score>=650:
                print("gold card")
            else:
                print("reject")
else:
    if income>=30000:
        if credit_score>=700:
            print("approve silver card ")
        else:
            print("reject")