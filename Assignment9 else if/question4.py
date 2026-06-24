subscription=input("enter the subscription type=").lower()
progress=int(input("enter the progress report="))
test_score=int(input("enter the test score="))
if subscription == "premium":
    if progress>=80:
        if test_score>=70:
            print("unlock certificate")
        else:
            print("retry test ")
    else:
        if subscription == "basic":
            if progress>=50:
                print("allow  limited acess")
            else:
                print("lock content")
else:
    print("deny access")
