# 3.

# =========================================================
#          MATRIX QUALITY CHECK SYSTEM
# =========================================================

# Scenario

# A manufacturing company records quality inspection values in
# matrix form. The Quality Control team wants a menu-driven
# application to analyze the inspection data and generate reports.

# The application should allow the user to:

# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Armstrong Numbers Row-wise
#    2. Count Palindrome Numbers Column-wise
#    3. Display Average of Each Row
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Armstrong Numbers Row-wise
#    -------------------------------------------
#    Count and display the number of Armstrong numbers
#    present in each row.

#    Examples:
#    153, 370, 371, 407

# 5. Choice 2 - Count Palindrome Numbers Column-wise
#    -----------------------------------------------
#    Count and display the number of palindrome numbers
#    present in each column.

#    Examples:
#    121, 131, 444, 1221

# 6. Choice 3 - Display Average of Each Row
#    --------------------------------------
#    Calculate and display the average of each row.

# 7. Choice 4 - Exit
#    --------------------------------------
#    Display:
#    "Thank You for Using Matrix Quality Check System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Armstrong Numbers Row-wise
# 2. Count Palindrome Numbers Column-wise
# 3. Display Average of Each Row
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 153 121 10
# 370 22 44
# 407 15 131

# Output:
# Row 1 Armstrong Count = 1
# Row 2 Armstrong Count = 1
# Row 3 Armstrong Count = 1

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Column 1 Palindrome Count = 0
# Column 2 Palindrome Count = 3
# Column 3 Palindrome Count = 2

# =========================================================





r1=int(input("row 1 : "))
c1=int(input("column 1 : "))

list1=[]
list3=[]
print("LIst 1 ")
for i in range(r1):
    temp=[]
    print("enter the column value")
    for j in range(c1):
        x=int(input("Enter the vlaue : "))
        temp.append(x)  
    list1.append(temp)    

    
print(list1)


while(1):
    print("1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
    print("4 : Exit")
    x=int(input("Enter ur choice : "))
    match x:
         case 1: 
              for i in  range(r1):
                   count=0
                   for j in range(c1):
                       x=str(list1[i][j])
                       l=len(x)
                       n=list1[i][j]
                       num=0
                       while n>0:
                            num+=(n%10)**l
                            n=n//10
                       if num==list1[i][j]:
                            count+=1     
                   print("Prime No in row ",i,"is : ",count)               
                        
         case 2 :              
              for i in  range(r1):
                   
                   count=0
                   
                   for j in range(c1):
                        k=list1[j][i]
                        n=0
                        while k>0:
                             n=n*10+k%10
                             k=k//10

                        if n==list1[j][i]:
                             count+=1
                   print("Column",i," : ",count)          
                        
                                                     
                        
         case 3 :              
              
              for i in  range(r1):
                   sum=0
                   for j in range(c1):
                        sum+=list1[i][j]
                   print("Average of Row ",i, " : ",sum/c1)     
                       
              
         case 4: print(list1)          
         case 5:
                  print("THank You")          
                  break
                                                       
                   
                        
    