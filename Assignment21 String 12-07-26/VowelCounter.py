# 1.Vowel Counter in Customer Feedback

#  A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

# Input: Enter feedback message: Hello Customer Service

# Output: Total vowels: 8

s=input("Enter the String").lower()
count=0
for i in s:
    if i in ['a','e','i','o','u']:
        count+=1
print("Total Vowel are :- ",count)        
    