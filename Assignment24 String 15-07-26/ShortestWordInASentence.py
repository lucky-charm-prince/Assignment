# 4. Program should work for both uppercase and lowercase letters.

#  Find the Shortest Word in a Sentence

# Telecom SMS Cost Optimization System

# A telecom company charges customers based on the length of words used in bulk SMS campaigns.

# The company wants to identify the shortest word in every message for analytics purposes.

# Write a Python program to find the shortest word from a given sentence.

# Input:

# ```
# Python is very easy to learn
# ```

# Output:

# ```
# is
import sys

x = sys.maxsize

s=input("Enter the String : ")
s=s.strip()
prev=0 
start=0

for i in s:
    if i==' ':
        size=start-prev
        if x>size:
            x=size
        prev=start+1    
    start+=1    
if x>(len(s)-prev-1):
    x=len(s)-1-prev

prev=0 
start=0
size1=x
y=0
for i in s:
    if i==' ':
        size=start-prev
        if size==size1:
            x=size
            print(s[prev:start])
            y=1
            break
        prev=start+1    
    start+=1    

if y==0:
    print(s[prev:len(s)])