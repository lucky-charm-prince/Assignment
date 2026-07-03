# 6.

# Next Prime Cabin Number Generator


# A luxury hotel gives only prime numbered cabins to VIP guests.


# Manager enters the last allotted cabin number.

# System must find the next available prime cabin number.


# Write a program using loops.


# Input:

# 24


# Output:

# Next Prime Cabin = 29

n=int(input("Enter the number : "))
if n>=1:
   n1=n+1
else :
   n1=2

while True :

    for i in range(2,n1//2+1):
        if n1%i==0:
            n1+=1
            break
    else:
        print("NextPrime is : ", n1)
        break    
