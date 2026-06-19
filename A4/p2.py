# Mobile price = 30000
# Down payment = 5000
# Interest rate = 10%
# Months = 10

# Expected Output:
# Remaining Amount = 25000
# Total with Interest = 27500
# Monthly EMI = 2750.0

mobile_price =int(input("Enter the mobile price: "))
down_payment =int(input("Enter the down payment: "))
interest_rate =int(input("Enter the interest rate: "))
months =int(input("Enter the number of months: "))
remaining_amount = mobile_price - down_payment
total_with_interest=remaining_amount+(mobile_price*interest_rate*months/12/100)
print("Remaining Amount = ",remaining_amount)
print("Total with Interest = ",total_with_interest)
total_emi=total_with_interest/months
print("Monthly EMI = ",total_emi)