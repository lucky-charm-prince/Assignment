import math

# Input:
# Total runs = 275
# Overs = 48.3

# Expected Output:
# Total Balls = 291
# Run Rate = 5.67


total_runs=int(input("Enter the total runs : "))
over=float(input("Total Over : "))
total_balls=int((math.floor(over)*6)+((over*10)%10))
print(total_balls)
x=((over*10)%10)/6
o=int(over)
print(o+x)
run_rate=(total_runs/(o+x))
print(run_rate)
