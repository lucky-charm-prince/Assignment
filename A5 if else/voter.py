#1. Smart Voting & ID Verification System
#   A government system verifies whether a citizen can vote and whether they have a valid ID.

#* If age ≥ 18 → Eligible to vote
#* If ID proof is available → Allowed inside booth

#Input:
#Enter age: 22
#Do you have ID (yes/no): yes

#Output:
#Eligible to vote
#Allowed inside booth



age=int(input("Enter your age : "))
if age>=18 :
    print("Eligible for vote")
    id_proff=input("DO you have the voter id Yes or NO").lower()
    if  id_proff=="yes":
        print("Allowed inside the booth")
    else:
        print("NOt Allowed for booth")
else:
    print("Not Eligible for vote")