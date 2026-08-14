# 4.

# =========================================================
#         MATRIX DIAGONAL ANALYSIS SYSTEM
# =========================================================

# Scenario

# A security company stores surveillance data in matrix form.
# The analyst wants a menu-driven application to examine the
# diagonal elements of the matrix and generate reports.

# The application should allow the user to:

# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Display Main Diagonal Elements
#    2. Display Secondary Diagonal Elements
#    3. Compare Main and Secondary Diagonal Sums
#    4. Exit

# 2. Read the size of a square matrix from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Display Main Diagonal Elements
#    -----------------------------------------
#    Display all elements present in the main diagonal.

# 5. Choice 2 - Display Secondary Diagonal Elements
#    ----------------------------------------------
#    Display all elements present in the secondary diagonal.

# 6. Choice 3 - Compare Main and Secondary Diagonal Sums
#    ---------------------------------------------------
#    Calculate the sum of both diagonals and display:

#    - Main Diagonal Sum
#    - Secondary Diagonal Sum
#    - Which diagonal has the greater sum
#    - Or whether both sums are equal

# 7. Choice 4 - Exit
#    -----------------------------------------
#    Display:
#    "Thank You for Using Matrix Diagonal Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Enter size of matrix: 3

# Enter matrix elements:

# 1 2 3
# 4 5 6
# 7 8 9

# Menu
# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# Enter your choice: 1

# Output:
# Main Diagonal Elements:
# 1 5 9

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Secondary Diagonal Elements:
# 3 5 7

# ---------------------------------------------------------

# Enter your choice: 3

# Output:
# Main Diagonal Sum = 15
# Secondary Diagonal Sum = 15
# Both Diagonal Sums are Equal

# =========================================================


r1=int(input("row 1 : "))
c1=int(input("column 1 : "))

list1=[]
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
    print("1. Display Main Diagonal Elements")
    print("2. Display Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4 : Exit")
    x=int(input("Enter ur choice : "))
    match x:
         case 1: 
              
              for i in  range(r1):
                   print(list1[i][i],end=" ")
              
                        
         case 2 :              
              for i in  range(r1):
                   print(list1[i][abs(r1-i-1)],end=" ")
                  
                        
                                                     
                        
         case 3 :              
              sum1=0
              sum2=0
              for i in  range(r1):
                   sum1+=list1[i][i]
                   sum2+=list1[i][abs(r1-i-1)]
                   print("Main Daigonal Sum : ",sum1)
                   print("Second Daigonal Sum : ",sum2)
                   if sum1==sum2:
                        print("Both are equal ")
                   else:
                        print("Not Equal")     
                       
              
         case 4: print(list1)          
         case 5:
                  print("THank You")          
                  break
                                                       
                   
                        
     