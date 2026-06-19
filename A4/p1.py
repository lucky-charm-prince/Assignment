total_amount=int(input("Enter the total amount: "))
gst=int(input("Enter the GST percentage: "))
service_charge=int(input("Enter the service charge percentage: "))
frinds=int(input("Enter the number of friends: "))
final_bill=(total_amount*gst/100)+(total_amount*service_charge/100)+total_amount
print("The final bill is: ",final_bill)
each_person=final_bill/frinds
print("Each person has to pay: ",each_person)