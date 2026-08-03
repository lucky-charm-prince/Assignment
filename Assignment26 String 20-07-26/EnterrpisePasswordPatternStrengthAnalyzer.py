# # 7. Enterprise Password Pattern Strength Analyzer

# A cybersecurity company wants to validate advanced passwords.

# ## Conditions:

# * Minimum 10 characters
# * At least:

#   * 1 uppercase letter
#   * 1 lowercase letter
#   * 1 digit
#   * 1 special character
# * No consecutive repeating characters
# * No spaces allowed

# ### Input:

# ```text
# Pyth@n1234
# ```

# ### Output:

# ```text
# Strong Password
# ```

# ### Input:

# ```text
# Paaass@12
# ```

# ### Output:

# ```text
# Weak Password
# ```

# ---

s=input("Enter the String : ")
upper=0
lower=0
digit=0
specialCharacter=0
if len(s)>3:
    for i in range(len(s)):
        if '0'<=s[i]<='9':
            digit+=1
        elif "A"<=s[i]<='Z':
            upper+=1
            
        elif "a"<=s[i]<='z':
            lower+=1
        elif s[i]!=' ':
            specialCharacter+=1
        else:
            print("Weak Password")    
            break
        if (i>0) and (s[i]==s[i-1]):
            print("Weak Password")    
            break


    else:
        print("Strong Password")    
else:
    print("Weak Password")        


