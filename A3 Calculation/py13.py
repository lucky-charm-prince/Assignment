principle=int(input("Enter the principle amount : "))
rate=int(input("Enter the rate amount"))
time=int(input("Enter the Time period"))
x=1+(rate/100)

y=1
for i in range(1 , time+1):
    y=y*x

print(y)
total=principle*y
print(total-principle)
