# Input:
# Distance = 450 km
# Mileage = 15 km/litre
# Petrol price = 110/litre

# Expected Output:
# Petrol Used = 30.0 litres
# Total Cost = 3300.0

distace=int(input("Distance : "))
mileage=int(input("Mileage : "))
pertrol_price=int(input("Pertrol Price : "))
petrol_used=distace/mileage
print("Pertrol Used : ",petrol_used)
cost=petrol_used*pertrol_price
print("Total cost : ",cost)
