# 3.
# Industrial Sensor Peak Energy Monitoring System

# Problem Statement

# A factory machine records energy consumption at regular intervals.

# A peak is defined as a value greater than or equal to its neighbors.

# Tasks:

# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# If no peaks, return -1

# Test Case 1

# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2

# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1525
# Average = 25
# Difference = 10

# Test Case 3

# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0



traffic = [20, 40, 30, 60, 50]
arr=[]
for i in range(len(traffic)):
    if i==0:
        if len(traffic)==1 or traffic[i]>traffic[i+1]:
            arr.append(traffic[i])
    elif i==len(traffic)-1:
        if traffic[i]>traffic[i-1]:
            arr.append(traffic[i])
    else:
        if traffic[i+1]<traffic[i]>traffic[i-1]:
            arr.append(traffic[i])                
print("Peak : ",arr)            
sum=0
pro=0
peak=None
if len(arr)>0:
    pro=1
    peak=arr[len(arr)-1]-arr[0]

for i in arr:
    sum+=i**2
    pro+=i
    
    
avg=pro//len(arr)        
print("SquaerSum : ",sum)        
print("Average : ",avg)        
print("Peak Differce : ",peak)        