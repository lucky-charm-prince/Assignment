# 2.

# =========================================================
#             MATRIX ANALYSIS SYSTEM
# =========================================================


# A research laboratory stores experimental data in matrix form.
# Scientists want a program that can analyze the matrix and provide
# different statistics through a menu-driven application.

# The application should allow the user to:

# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Prime Numbers Row-wise
#    2. Count Perfect Numbers Column-wise
#    3. Display Row-wise Sum
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Prime Numbers Row-wise
#    ---------------------------------------
#    Count and display the number of prime numbers present
#    in each row of the matrix.

# 5. Choice 2 - Count Perfect Numbers Column-wise
#    --------------------------------------------
#    Count and display the number of perfect numbers present
#    in each column of the matrix.

#    Note:
#    A perfect number is a number that is equal to the sum
#    of its proper divisors.

#    Examples:
#    6  = 1 + 2 + 3
#    28 = 1 + 2 + 4 + 7 + 14

# 6. Choice 3 - Display Row-wise Sum
#    --------------------------------
#    Calculate and display the sum of each row.

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 2 4 5
# 6 7 8
# 11 28 13

# Output:
# Row 1 Prime Count = 2
# Row 2 Prime Count = 1
# Row 3 Prime Count = 2

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Pehn Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 2

# Output:
# Column 1 Perfect Number Count = 1
# Column 2 Perfect Number Count = 1
# Column 3 Perfect Number Count = 0

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 3

# Output:
# Row 1 Sum = 11
# Row 2 Sum = 21
# Row 3 Sum = 52

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Analysis System

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
    print("1 : prime Count row wise : ")
    print("2 : Perfect NUmber ")
    print("3 : Sum Row Wise")
    print("4 : Show List")
    print("5 : Exit")
    x=int(input("Enter ur choice : "))
    match x:
         case 1: 
              for i in  range(r1):
                   count=0
                   for j in range(c1):
                        if list1[i][j]==2:
                             count+=1
                        else: 
                             for k in range(2,list1[i][j]//2+1):
                                  if  list1[i][j]%k==0:
                                     break
                             else:
                                      count+=1
                   print("Prime No in row ",i,"is : ",count)               
                        
         case 2 :              
              for i in  range(r1):
                   
                   count=0
                   
                   for j in range(c1):
                        k=list1[j][i]
                        total=0
                        for x in range(1,k//2+1):
                             if k%x==0:
                                  total+=x

                        if total==k:
                             count+=1
                   print("Column",i," : ",count)          
                        
                                                     
                        
         case 3 :              
              
              for i in  range(r1):
                   sum=0
                   for j in range(c1):
                        sum+=list1[i][j]
                   print("sum of Row ",i, " : ",sum)     
                       
              
         case 4: print(list1)          
         case 5:
                  print("THank You")          
                  break
                                                       
                   
                        
                             
        
                


    