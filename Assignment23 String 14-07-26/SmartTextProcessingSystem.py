# QNo 8:--
# SMART TEXT PROCESSING SYSTEM

# A software company is developing a Smart Text Processing System for
# handling user messages. Different users require different text
# transformations. To avoid creating separate applications, the company
# wants a menu-driven program where users can select operations according
# to their requirements.
 
# The system should continue executing until the user selects Exit.

# ====================================================== MENU 
# ======================================================

# ===== Smart Text Processing System =====

# 1.  Reverse Complete String
# 2.  Reverse Every Word
# 3.  Reverse Word Order
# 4.  Exit

# ====================================================== Choice 1 :

# Conditions: - Reverse the complete string - Ignore extra spaces - Keep
# special characters (@,#,$,%) in their original positions - Do not use
# built-in reverse functions

# Example: Input: ja@va#py

# Output: yp@av#aj

# Test Case 1: ab@cd#ef Output: fe@dc#ba

# Test Case 2: py@th#on Output: no@ht#yp

# Test Case 3: java@proOutput : orpa@vaj

# ====================================================== Choice 2 :

# Conditions: - Reverse every word separately - Words containing digits
# should not be reversed - Ignore extra spaces between words - First   
# letter of each reversed word should become uppercase

# Example: Input: java is easy123 programming

# Output: Avaj Si easy123 Gnimmargorp

# Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
# Repoleved

# Test Case 2: hello java99 world Output: Olleh java99 Dlrow

# ====================================================== Choice 3 :

# Conditions: - Reverse order of words - Remove duplicate words - Ignore
# case while checking duplicates - Keep only first occurrence

# Example: Input: Java python Java react Python

# Output: React Python Java

# Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

# Test Case 2: Python React Java Python React Output: Java React Python

# ====================================================== Choice 4
# ======================================================

# Program Closed Successfully

# s=input("Enter the String : ")
# s1=""
# s2=""
# for i in s :
#     if i.isalpha():
#         s1+=i
#     else:
#         s2+=i
# x=s1[::-1]
# i=0
# j=0
# s3=""
# for k in s:
#     if not(k.isalpha()):
#         s3+=s2[i]
#         i+=1
#     else:
#         s3+=x[j]
#         j+=1
# print(s3)




# Conditions: - Reverse every word separately - Words containing digits
# should not be reversed - Ignore extra spaces between words - First   
# letter of each reversed word should become uppercase

# Example: Input: java is easy123 programming

# Output: Avaj Si easy123 Gnimmargorp

# Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
# Repoleved

# Test Case 2: hello java99 world Output: Olleh java99 Dlrow

# s=input("Enter the String : ")
# s1=""
# digitContaion=0
# start=-1
# for i in range(0,len(s)):
#     if s[i]==' ':
        
#         for j in range(start+1,i):
#             if '0'<=s[j]<='9':
#                 digitContaion=1
        
#         if digitContaion==0:
#             rev=""
#             for j in range(start+1,i):
#                 rev=s[j]+rev
#             s1+=rev+" "    
#         else:
#             s1+=s[start:i]
#         start=i    

# digitContaion=0
# for j in range(start+1,len(s)):
#     if '0'<=s[j]<='9':
#                 digitContaion=1
# if digitContaion==0:
#             rev=""
#             for j in range(start+1,len(s)):
#                 rev=s[j]+rev
#             s1+=rev+" "    
# else:
#         s1+=s[start:i]
#         start=i                

# print(s1)        



# ====================================================== Choice 3 :

# Conditions: - Reverse order of words - Remove duplicate words - Ignore
# case while checking duplicates - Keep only first occurrence

# Example: Input: Java python Java react Python

# Output: React Python Java

# Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

# Test Case 2: Python React Java Python React Output: Java React Python


s=input("Enter the String : ")

word=s.split()
s1=""
for i in word:
    s1=i+" "+s1
word=s1.split()

print(word)
s1=""


for i in range(0,len(word)):
    count=0
    for j in range(i+1,len(word)):
        if word[i].lower()==word[j].lower():
            count+=1
    if count==0:
        
        s1+=word[i]+" "
s1=s1.strip()
print(s1)