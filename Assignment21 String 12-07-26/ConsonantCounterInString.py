# 4.
# Consonant Counter in Student Name Record

# A school management system wants to count how many consonants are present in student names.

# Input: Enter student name: Ajay Singh Thakur

# Output: Total consonants: 11

# NOTE:

# Ignore case sensitivity (treat A and a same)
# Consider only English alphabets for vowel/consonant counting
# Vowels: A, E, I, O, U

s=input("Enter the string : ").lower()
count=0
for i in s:
    if i not in ['a','e','i','o','u']:
    
        if ord(i)>=97 and ord(i)<=122:
            count+=1
print("Total consonants : ",count)    



