# 7.
# Vehicle Number Plate Checker

# The traffic department wants to validate vehicle registration numbers.

# Conditions:
# - First 2 characters should be alphabets
# - Next 2 should be digits
# - Total length should be 10

# Input:
# Enter vehicle number: MP04AB1234

# Output:
# Valid Vehicle Number

s=input("Enter the NUmber : ").upper()
if len(s)==10:
    if 'A'<=s[0]<='Z' and 'A'<=s[1]<='Z':
        if '0'<=s[2]<='9' and '0'<=s[3]<='9':
            if 'A'<=s[4]<='Z' and 'A'<=s[5]<='Z':
                for i in range(6,len(s)):
                    if ord(s[i])<48 or ord(s[i])>57:
                        print("NOt Valid")
                        break
                else:
                    print("valid NUmber")    
            else:
                print("NOt Valid")        
        else:
            print("NOt Vlaid number")        
    else:
            print("NOt Vlaid number")        
else:
            print("NOt Vlaid number")                    
