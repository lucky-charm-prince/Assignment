# 2.Employee Salary Processing
# Store employee salaries in a List and calculate details.

# Requirements:

# Store salaries
# Find average salary
# Display salaries greater than average
# Remove salaries below 15000

# Test Cases:

# Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
# Input: [15000, 15000, 15000] → Average = 15000
# Input: [5000, 7000] → Remaining List = []


n=list(map(int,input("Enter the list : ").split(",")))
avg=0
total=0
new=[]
for i in n:
    total+=i

avg=total//len(n)
print("Average : ",avg)    
for i in n:
    if i>avg:
        print(i,end=" ")
    if i>15000:
        new+=[i]

print("\n",new)        
            
