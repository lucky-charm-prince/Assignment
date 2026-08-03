# 4.
# Employee ID Validator

# A company wants to validate employee IDs before storing them in the database.

# Conditions:
# - ID must start with "EMP"
# - Total length should be 8
# - Remaining characters should be digits only

# Input:
# Enter Employee ID: EMP10234

# Output:
# Valid Employee ID

s=input("Enter the Employee Id ")
if len(s)==8:
    if s[0]=='E' and s[1]=='M' and s[2]=='P':
        for i in range(4,len(s)):
            if s[i]>'9' or s[i]<'0':
                print("INvalid Employee Id ")
                break
        else:
            print("Valid Employee ID")    
    else:
            print("InValid Employee ID")            
else:
     print("Invalid Employee id ")            

