# 5. Next Prime ID Generator – Smart Version

# A company gives prime numbered employee IDs to premium staff.

# Manager enters current ID.
# System must:

# - Find next prime number after current ID
# - Find difference between current ID and next prime

# Write a program using loops.

# Input:
# 20

# Output:
# Next Prime ID = 23
# Gap = 3


n=int(input("Enter the number : "))
num=n
if n==0:
    num+=2
else:

    num+=1  

while True:    
    for i in range(2,num//2+1):
        if num%i==0:
            num+=1
            break

    else:
        break        

print("next Prime Number is : ",num)
print("Gap : ",num-n)