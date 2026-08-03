# 6.
#  Advanced Student Registration Data Processing System

# A national university is developing an intelligent registration portal.
# Students enter registration codes using uppercase letters, lowercase
# letters, digits, and special symbols. Due to inconsistent data entry,
# the administration wants the system to standardize and process the
# information before storing it.

# Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
# alphabets and digits - Convert all alphabets to lowercase - Remove
# duplicate alphabets - Arrange alphabets in ascending order - Arrange
# digits in descending order - Display alphabets first and digits later -
# If no digits are found, display “No Digits Found”

# Test Case 1 Input: Enter registration code: zBc@638

# Output: Result: bcz863

# Test Case 2 Input: Enter registration code: 5Br$dE654b

# Output: Result: bder6554

# Test Case 3 Input: Enter registration code: A9@C3d#6B1a

# Output: Result: abcd9631

# Test Case 4 Input: Enter registration code: X#X@M2A4x7

# Output: Result: amx742

# Test Case 5 Input: Enter registration code: r@T#y

# Output: Result: rty No Digits Found

s=input("Enter the String : ").lower()
s1=""
s2=""
for i in s:
    if 'a'<=i<='z':
        for j in s1:
            if i==j:
                break
        else:
            s1+=i    
    if '0'<=i<='9':
        s2+=i 


# print(s1,s2)
finalString=""
if len(s1)>0:
    while len(s1)>0:
        k=s1[0]
        y=0
        for j in range(len(s1)):
            if k>s1[j]:
                k=s1[j]
                y=j
        x=s1[0:y]+s1[y+1:len(s1)]
        
        s1=x
        
        finalString+=k        

print(finalString,end="")


numberString=""
if len(s2)>0:
    while len(s2)>0:
        k=s2[0]
        y=0
        for j in range(len(s2)):
            if k>s2[j]:
                k=s2[j]
                y=j
        x=s2[0:y]+s2[y+1:len(s2)]
        
        s2=x
        
        numberString=k+numberString        
        

if len(numberString)>0:
    print(numberString)
else:
    print("No digit foundn")    
