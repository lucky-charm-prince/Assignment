# 6.

# Product Code Verification System

# An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

# Conditions:
# - Ignore spaces
# - Ignore case sensitivity

# Input:
# Enter first product code: Dormitory
# Enter second product code: Dirty Room

# Output:
# Both Product Codes are Matching
a=input("Enter the first product code : ").lower()
b=input("Enter the Second product code : ").lower()

x=""
y=""
for i in a:
    if i!=' ':
        x+=i
for i in b:
    if i!=' ':
        y+=i
print(x,y)


if len(x)==len(y):
          for i in x:
                xcount=0
                ycount=0
                if i==' ':
                    continue
                for j in range(0,len(x)):
                    if x[j]==i:
                        xcount+=1
                for k in range(0,len(y)):
                    if y[k]==i:
                        ycount+=1
                if xcount!=ycount:
                    print("Not Same")        
                    break
                
                xcount=0
                ycount=0    

          else :
                print("Equal")
else:
     print("not equal")                