# 2.  Corporate Employee Short ID Generator

# A multinational company wants to automatically generate short IDs for
# employees while creating official email accounts. The system should take
# the employee’s full name and create an ID using the first character of
# each word.

# Conditions: - Take first character of every word - Convert all
# characters to uppercase

# Input: Enter employee name: ajay singh thakur

# Output: Employee Short ID: AST

s=input("Enter the employee name : ")
s1=""
if (len(s)>0) and (s[0]!=' '):
    if 'a'<=s[0]<='z':
        s1+=chr(ord(s[0])-32)
    else:
        s1+=s[0]
    


for i in range (1,len(s)):
        if s[i-1]==' ' and (('a'<=s[i]<='z') or ('A'<=s[i]<='Z')):
            if 'a'<=s[i]<='z':
                s1+=chr(ord(s[i])-32)
            else:
               s1+=s[i]

print(s1)
    


