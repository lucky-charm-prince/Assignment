# 5.
# Advanced Password Security Checker

# A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

# Conditions: Password must:

# Start with an uppercase letter
# End with a digit
# Contain at least 2 digits
# Contain at least 1 special character (@ # $ % & *)
# Must not contain spaces
# Length should be between 8 and 15 characters

# Input: Enter password: Python@45

# Output: Secure Password

s=input("Enter the String : ")
digitcount=0
specialcount=0
if len(s)>=8 and len(s)<=15:
    if ord(s[0])>=67 and ord(s[0])<=97:
        if ord(s[len(s)-1])>=48 and ord(s[len(s)-1])<=57:
            for i in s :
                if ord(i)>=48 and ord(i)<=57:
                    digitcount+=1
                if i in ['@','#','$','%',"*"]:
                    specialcount+=1
                if i==' ':
                    print("Space found break here")        
                    break
            else:
                if digitcount>=2 and specialcount>=1:
                    print("Valid password")
                else:
                    print("INvalid password ")    
        
        else:
            print("Last Digit not end with digit")
    else:
        print("Not Start with upper case letter")    
        
else:
    print("Length of password between 8 to 15 charatceter")        


