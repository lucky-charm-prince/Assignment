# 5.
# Palindrome Product Code Checker

# A factory wants to identify whether a product code reads the same forward and backward.

# Input:
# Enter product code: MADAM

# Output:
# Palindrome Code

# Input:
# Enter product code: PRODUCT

# Output:
# Not a Palindrome Code
s=input("Enter the String : ")
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")    