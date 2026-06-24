# 12. Restaurant Bill with GST System

# A restaurant applies GST based on the total bill amount:

# * Up to ₹1000 → 5% GST
# * ₹1001 to ₹5000 → 12% GST
# * Above ₹5000 → 18% GST
#   Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

# Write a Python program to calculate the final bill.

# Input:
# Enter bill amount: 4000

# Output:
# Final Bill Amount: ₹4680

bill_amount=int(input("enter the bill amount="))
if bill_amount<=1000:
    print("final bill amount=",bill_amount+(bill_amount*5)//100)
elif bill_amount>=1001 and bill_amount<=5000:
    print("final bill amount=",200+(bill_amount+(bill_amount*12)//100))
else:
    print("final bill amount=",bill_amount+(bill_amount*18)//100)