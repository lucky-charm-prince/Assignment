age=65
severity="critical".lower()
insurance="yes"
if severity=="critical":
    if age>=60:
        print("immediate ice")
    else:
        print("emergency ward")
elif severity=="moderate":
    if insurance=="yes":
        print("priority treatment")
    else:
        print("genral queue")
else:
    if age<10:
        print("pediatric priority")
    else:
        print("assign wait")