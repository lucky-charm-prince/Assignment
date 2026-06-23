# 9. Library Access System
#    A library checks:

# * If membership is active → Entry allowed
# * If books issued < 3 → Can issue more books

# Input:
# Membership active (yes/no): yes
# Books issued: 2

# Output:
# Entry allowed
# Can issue more books
membership=input("Membership is Active Yes or NO :").lower()
if membership=="yes":
    print("Entry Allowed")
    book_issue=int(input("Enter the book issueed :"))
    if book_issue<3:
        print("Can issue more books")
    else:
        print("Not issued more books")    
else:
    print("Not Membership")        