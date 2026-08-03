# 5. Website URL Verification System

# A software company is developing an automated website registration
# portal. Before saving a website address, the system must verify whether
# the URL follows the required company format.

# Conditions: - Must start with www - Must end with .com

# Input: Enter website: www.amazon.com

# Output: Valid Website

s=input("Enter the website url : ").lower()

if len(s)>7:
    if s[0]=='w' and  s[1]=='w' and  s[2]=='w' and s[len(s)-1]=='m' and s[len(s)-2]=='o' and s[len(s)-3]=='c' and s[len(s)-4]=='.':
        print("valid")
        
    else:
        print("INValid")
else:            
    print("Invalid")        