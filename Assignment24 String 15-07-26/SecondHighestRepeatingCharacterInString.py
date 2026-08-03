# 8.
# Find the Second Highest Repeating Character in a String

# Social Media Trend Analysis System

# A social media company analyzes hashtags and user comments to identify trending character patterns.

# The analytics team wants a Python program to find the character with the second highest frequency in a given string.

# This helps detect secondary trending patterns in user activity.

# Input:

# aaabbbbccddeee

# Output:

# e

# Explanation:

# b occurs 4 times → highest
# e occurs 3 times → second highest

# Condition:

# Program should work for both uppercase and lowercase letters.
# Spaces should be ignored.
# If no second highest frequency exists, print:
# Second highest repeating character not found

s=input("Enter the String : ")
maxCount=0
count=0
if len(s)>0:
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            if maxCount<count:
                maxCount=count
            count=1    

if maxCount<count :
    maxCount=count


secondMax=0
count=1
x=None
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        if secondMax<=count and count<maxCount:
            x=s[i-1]
            
            secondMax=count
        count=1    

if secondMax<=count and count<maxCount:
            x=s[len(s)-1]
            secondMax=count
            count=1    
print(x)            