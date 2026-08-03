# 5.
# Cybercrime Log Analysis System

# A cybersecurity company monitors encrypted login activity stored as character-based security logs.

# During investigation, analysts need to identify the last character that repeats in the log sequence.
# This helps detect the most recent duplicated activity pattern before a possible security breach.

# Write a Python program to find the last repeating character in a given string.

# If no  character exists, print:

# No repeating character found
# Input:
# abccdbefga
# Output:
# a

s=input("Enter the input : ")
s1=""
for i in s:
    s1=i+s1

#print(s1) 
k=0
for i in range(0,len(s1)):
    count=0
    for j in range(i,len(s1)):
        if s1[i]==s1[j]:
            count+=1
        if count==2:
            k=1
            print(s1[i])
            break
    if k==1:
        break    
if k==0:
    print("No Repeated Character Found")            

