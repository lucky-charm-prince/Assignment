# 2.
# Secure Password Analysis

# A cybersecurity team wants to identify pairs of passwords having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 3

# Explanation

# ("abc","de")
# ("abc","fg")
# ("de","fg")

n=int(input("Size of list : "))
password=[]
for i in range(n):
    x=input("passsword : ")
    password.append(x)
count=0    
print(password)    
for i in range(n):
    for j in range(i+1,n):
        x=len(password[i])
        s=password[i]
        for k in range(x):
            if s[k] in password[j]:
                break
        else:
            print(password[i],password[j])
            count+=1    
print(count)            