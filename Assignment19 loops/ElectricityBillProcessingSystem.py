# 10.
# Electricity Bill Processing System (Multi-House)

# An electricity board processes bills for multiple houses in a society.

# Write a program to:

# - Read number of houses n
# - For each house:
#     - Read units consumed
#     - Calculate bill using slab rates:

#         First 100 units      → ₹5 per unit  
#         Next 100 units      → ₹7 per unit  
#         Above 200 units     → ₹10 per unit  

#     - Apply conditions:
#         - If bill > ₹2000 → add 10% surcharge  
#         - If units < 50 → give ₹100 subsidy  

#     - Print bill for each house

# - After processing all houses:
#     - Print total bill collected
#     - Print highest bill

# ---

# Input:
# 3
# 120
# 250
# 40

# Output:
# House 1 Bill = 640
# House 2 Bill = 1700
# House 3 Bill = 100

# Total Collection = 2440
# Highest Bill = 1700
totalSum=0
max=0
x=int(input("Enter the number : "))

for i in range(1,x+1):
    n=int(input("Enter the unit : "))
    total=0    

    if n<=100:
       total=n*5
       if n<50:
          total-=100
       n=0
    else:
       total=100*5
       n=n-100
       if n<=100:
          total=total+n*7
          n=0
       else:
          total=total+100*7
          n=n-100
          if n>0:
            total=total+n*10
            n=0
    if total>2000:
       total=total+total*0.1        
    if total>max:
       max=total
    totalSum+=total   
print("total collection : ",totalSum)  
print("Highest collection : ",max)  

