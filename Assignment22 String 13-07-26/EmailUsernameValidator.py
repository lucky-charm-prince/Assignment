# 1.
# Email Username Validator

# A company wants to check whether an employee email username is valid before creating an official account.

# Conditions:
# - Username should start with a letter
# - Username can contain letters, digits, underscore (_)
# - No spaces allowed
# - Length should be between 5 and 12 characters

# Input:
# Enter username: ajay_123

# Output:
# Valid Username


s=input("Enter the uesrname : ").lower()
if 5<=len(s)<=12:
    if 'a'<=s[0]<='z':
        for i in range(1,len(s)):
            if (('0'<=s[i]<='9') or ('a'<=s[i]<='z') or (s[i]=='_')):
                
                continue
            else:

                print("NOt Valid")
                break
        else:
            print("Valid User Name")
    else:
            print("Valid User Name")
else:
            print("Valid User Name")
 