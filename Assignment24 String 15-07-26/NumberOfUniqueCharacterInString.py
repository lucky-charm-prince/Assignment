# 5. Find the Number of Unique Characters in a String

# Password Strength Analyzer

# A cybersecurity company checks password strength based on the number of unique characters present.

# Passwords containing more unique characters are considered more secure.

# Write a Python program to count the number of unique characters in a string.

# Input:

# ```
# aabbccdde
# ```

# Output:

# ```
# 5
# ```

s=input("Enter the String : ")
count=0
if len(s)>0:
    count=1

for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        count+=1
print(count)        