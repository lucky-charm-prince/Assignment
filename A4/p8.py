
# Input:
# Principal = 10000
# Rate = 5%
# Time = 2 years

# Expected Output:
# Amount after interest = 11025.0
amount=int(input("Enter the amount : "))
rate=int(input("Rate : "))
time=int(input("Enter the time : "))

x=(1+rate/100)**time
toatl_intrest=x*amount
print(toatl_intrest)
