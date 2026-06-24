attendance_per=int(input("enter the attendance percentage="))
if attendance_per>70:
    print("eligible")
elif attendance_per>=60 and attendance_per<=74:
    print("eligible with warning")
else:
    print("not eligible")