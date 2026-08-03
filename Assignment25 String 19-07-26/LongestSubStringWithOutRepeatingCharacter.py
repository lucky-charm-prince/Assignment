# 1.
# Find the Longest Substring Without Repeating Characters
# Cybersecurity Session Tracking System

# A cybersecurity company monitors user session IDs generated during secure login sessions.

# To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

# Input:
# abcabcbb
# Output:
# abc

s=input("Enter the String : ")

s2=""
for i in range(0,len(s)):
    s1=""
    for j in range(i,len(s)):
        if s[j] not in s1:
            s1+=s[j]
        else:
            break 
    if len(s1)>len(s2):
        s2=s1
print(s2)               