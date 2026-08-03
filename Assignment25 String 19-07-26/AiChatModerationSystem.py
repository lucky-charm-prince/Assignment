# 8.
# AI Chat Moderation System

# A social media company is developing an AI-based chat moderation system that analyzes user messages in real time.

# During analysis, the system must identify special symmetric words (palindromes) because they are used as secret tags in internal testing.

# A palindrome word is a word that reads the same forward and backward.

# Write a Python program to find the first palindrome word present in the sentence.

# If no palindrome word exists, print:

# No palindrome word found
# Input:
# madam and arun went to level racecar station
# Output:
# madam


s=input("Enter the String : ")
word=s.split()
for i in word:
    
    k=len(i)-1
    for j in range(0,len(i)//2):
        if i[j]!=i[k]:
            break
        k-=1
    else:
        print(i)
        break