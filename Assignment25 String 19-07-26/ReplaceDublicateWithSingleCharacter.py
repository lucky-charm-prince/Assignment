# 3.
# Replace Consecutive Duplicate Characters with Single Character
# Data Compression System

# A cloud storage company wants to reduce unnecessary repeated characters in text logs.

# Write a Python program that replaces consecutive duplicate characters with a single occurrence.

# Input:
# aaabbbccccdddaa
# Output:
# abcda


s=input("Enter the String : ")
s1=""
for i in range(1,len(s)):
    print(i)
    if s[i-1]!=s[i]:
        s1+=s[i-1]


if s1[len(s1)-1]!=s[len(s)-1]:
            s1+=s[len(s)-1]
            print("Yes")
print(s1)                            