# 6.
# Railway Ticket PNR Analyzer

# A railway department wants to verify whether a PNR number is valid.

# Conditions:
# - PNR must start with "PNR"
# - Total length should be 12 characters
# - Remaining characters should be digits

# Input:
# Enter PNR: PNR123456789

# Output:
# Valid PNR Number

s=input("Enter the pne  number : ")
if len(s)==12:
    if s[0]=='P' and s[1]=='N' and s[2]=='R':
        for i in range(3,len(s)):
            print(s[i])
            if ord(s[i])<48 or ord(s[i])>57:
                print("NOt Valid PNR")
                break
        else:
            print("Valid PNR")    
    else:
        print("NOt a valid PNR")  
     
else:
    print("NOt a valid pnr")    
