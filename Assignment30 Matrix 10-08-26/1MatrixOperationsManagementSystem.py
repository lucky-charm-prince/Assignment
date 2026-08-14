# 1.
# =========================================================
#         MATRIX OPERATIONS MANAGEMENT SYSTEM
# =========================================================


# A data analysis company stores numerical information in matrix form.
# To help employees perform matrix-related operations efficiently,
# the company wants a menu-driven application.

# The application should allow the user to:

# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# The user must enter the number of rows, columns, and all matrix
# elements. The program should perform the selected operation and
# display the result.

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user chooses Exit.

#    1. Add Two Matrices
#    2. Subtract Two Matrices
#    3. Compare Two Matrices
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all elements of Matrix A and Matrix B from the user whenever
#    required.

# 4. Based on the user's choice:

#    Choice 1 - Add Two Matrices
#    --------------------------------
#    Add corresponding elements of both matrices and display
#    the resultant matrix.

# 5. Choice 2 - Subtract Two Matrices
#    --------------------------------
#    Subtract corresponding elements of Matrix B from Matrix A
#    and display the resultant matrix.

# 6. Choice 3 - Compare Two Matrices
#    --------------------------------
#    Check whether both matrices are equal.

#    Two matrices are considered equal if:
#    - They have the same dimensions.
#    - Corresponding elements are equal.

#    Display:
#    "Matrices are Equal"
#    or
#    "Matrices are Not Equal"

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Operations Management System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 1

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 5 6
# 7 8

# Result Matrix:
# 6 8
# 10 12

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 3

# Enter number of rows: 2
# Enter number of columns: 2

# Enter Matrix A:
# 1 2
# 3 4

# Enter Matrix B:
# 1 2
# 3 4

# Output:
# Matrices are Equal

# ---------------------------------------------------------

# Menu
# 1. Add Two Matrices
# 2. Subtract Two Matrices
# 3. Compare Two Matrices
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Operations Management System

# =========================================================

r1=int(input("row 1 : "))
c1=int(input("column 1 : "))
r2=int(input("row 2 : "))
c2=int(input("colummn 2 : "))
list1=[]
list2=[]
list3=[]
if c1==r2:
    r3=r1
    c3=c2
    print("LIst 1 ")
    for i in range(r1):
        temp=[]
        print("enter the column value")
        for j in range(c1):
            x=int(input("Enter the vlaue : "))
            temp.append(x)  
        list1.append(temp)    
    print("List 2 ")
    for i in range(r2):
        temp=[]
        print("enter the column value")
        for j in range(c2):
            x=int(input("Enter the vlaue : "))
            temp.append(x)  
        list2.append(temp)    
    for i in range(r3):
            temp=[]
            
            for j in range(c3):
                x=0
                temp.append(x)  
            list3.append(temp)        
    print(list1)
    print(list2)
    print(list3)


    while(1):
        print("1 : Add Two Matrices")
        print("2 : Subtract Two Matrices")
        print("3 : Compare Two Matrices")
        print("4 : Show List")
        print("5 : Exit")
        x=int(input("Enter ur choice : "))
        match x:
             case 1: 
                  for i in  range(r1):
                       for j in range(c1):
                            list3[i][j]=list1[i][j]+list2[i][j]
             case 2 :              
                  for i in  range(r1):
                       for j in range(c1):
                            list3[i][j]=list1[i][j]-list2[i][j]    
             case 3 :              
                  k=0
                  for i in  range(r1):
                       for j in range(c1):
                            if list1[i][j]!=list2[i][j]:                                     
                                print("NOt Equal")
                                k+=1
                                break
                       if k!=0:
                            break    
                  else:
                       print("BOth are Equal")
             case 4: print(list3)          
             case 5:
                      print("THank You")          
                      break
                                                           
                       
                            
                             
        
                


    