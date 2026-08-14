
# 3.

# MATRIX PERFORMANCE EVALUATION SYSTEM

# A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

# The HR department wants a menu-driven application to analyze employee performance.

# Menu
# 1. Find Employee with Highest Total Score
# 2. Find Month with Lowest Average Score
# 3. Display Employee-wise Maximum Score
# 4. Exit
# Requirements
# Choice 1 – Find Employee with Highest Total Score
# Calculate the sum of each row.
# Display the employee number having the highest total score.
# Choice 2 – Find Month with Lowest Average Score
# Calculate the average of each column.
# Display the month having the lowest average score.
# Choice 3 – Display Employee-wise Maximum Score
# Find and display the maximum value present in each row.
# Sample Input
# 10 20 30
# 40 50 60
# 25 35 45
# Output
# Employee 2 has Highest Total Score = 150

# Month 1 Average = 25
# Month 2 Average = 35
# Month 3 Average = 45

# Employee 1 Max Score = 30
# Employee 2 Max Score = 60
# Employee 3 Max Score = 45


r1=int(input("row : "))
c1=int(input("column : "))
arr=[]
for i in range(r1):
    temp=[]
    print("Enter the row ",i,"value : ")
    for j in range(c1):
        x=int(input("value : "))
        temp.append(x)
    arr.append(temp)
print(arr)        

while 1:
    print("----------------------------------------------------------------------------------------------------------")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")
    x=int(input("Enter ur choice : "))
    match x:
        case 1 :
            max=0
            id=-1
            for i in range(r1):
                temp=0
                for j in range(c1):
                    temp+=arr[i][j]
                if temp>max:
                    id=i
                    max=temp
            print("Employee", id+1," has Highest Total Score : ",max)        

        case 2:
            for i in range(r1):
                temp=0
                for j in range(c1):
                    temp+=arr[j][i]
                print("Month", i,"Average",temp//3)
        case 3:
            for i in range(r1):
                max=arr[i][0]
                for j in range(c1):
                    if arr[i][j]>max:
                        max=arr[i][j]
                print("Employee ", i,"max scrore : ", max)
        case 4:
            print("Thank you")        
            break
                
