# 5. Banking Security System
#    A bank validates login attempt:

# * If username is "admin" → Valid user
# * If password length ≥ 8 → Strong password

# Input:
# Enter username: admin
# Enter password: secure123

# Output:
# Valid user
# Strong password

username=input("Enter the user name : ").lower()
if username=="admin":
    print("Valid User")
    password=input("Enter the passsword")
    if len(password)>=8:
        print("Strong Password")
    else:
        print("Simple Password")    
else:
    print("Invalid Password")