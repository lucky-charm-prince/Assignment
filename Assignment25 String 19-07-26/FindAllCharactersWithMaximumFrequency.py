# 4.

# Find All Characters with Maximum Frequency
# Website Traffic Analysis System

# A web analytics company tracks user activity symbols in server logs.

# The company wants to identify all characters having the maximum frequency in the given string.

# Input:
# aabbbccddd
# Output:
# b d

maxcount=0
s=input("Enter the String : ")
count=1
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        count+=1
        
    else:
        if count>maxcount:
            maxcount=count
        count=1
if count>=maxcount:
            
            maxcount=count
if len(s)==0:
      maxcount=0
print(maxcount)


for i in range(0,len(s)):
      count=0
      for j in range(i,len(s)):
            if s[i]==s[j]:
                  count+=1
      if count==maxcount:
            print(s[i],end=" ")           