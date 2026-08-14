# 6.

#  Frequency Count of Elements (Advanced Scenario-Based Problem)


# A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).

# The department wants to analyze:

# * How many times each option was selected
# * Most popular option
# * Least popular option
# * Detect invalid entries (negative numbers or zeros)

# ---

#  Requirements

# Write a Python program to:
# 6. Find the least frequently selected option (excluding invalid data)
# 7. Store frequency in a dictionary

# ---


# NOTE:
# * Avoid using built-in `Counter`

# ## Input Format

# A list of integers representing responses.

# ---

# # Scenario 1: Normal Survey Data

# ## Input

# [1, 2, 2, 3, 3, 3, 4, 1, 2]

# ## Output

# ```
# Frequency Count:
# 1 → 2
# 2 → 3
# 3 → 3
# 4 → 1

# Most Frequent: 2 or 3 (tie)
# Least Frequent: 4
# ```

# ---

# # Scenario 2: Data with Invalid Entries

# ## Input

# [ ]

# ## Output

# ```
# Invalid Entries Ignored: [-1, 0, -5]

# Frequency Count:
# 1 → 1
# 2 → 2
# 3 → 3
# 4 → 1

# Most Frequent: 3
# Least Frequent: 1 or 4
# ```

# ---

# # Scenario 3: Highly Skewed Data

# ## Input

# [5, 5, 5, 5, 2, 2, 1]

# ## Output

# ```
# Frequency Count:
# 1 → 1
# 2 → 2
# 5 → 4

# Most Frequent: 5
# Least Frequent: 1
# ```

# ---

# # Scenario 4: All Same Values

# ## Input

# [7, 7, 7, 7, 7]

# ## Output

# ```
# Frequency Count:
# 7 → 5

# Most Frequent: 7
# Least Frequent: 7
# ```

# ---

# # Scenario 5: Empty / Invalid Only Data

# ## Input

# [-1, 0, -3]

# ## Output

# ```
# No valid data found
# ```
 
# --
import sys
n=list(map(int,input("Enter the list : ").split(", ")))
x=[]
y=[]
maxCount=0
minCount=sys.maxsize
for i in n:
    if  i>0:
        
            if i not in x:
                x.append(i)
                count=0
                for j in n:
                    if i==j:
                        count+=1
                if count>maxCount:
                     maxCount=count
                if minCount>count:
                      minCount=count                
                y.append(count)       

for a,b in zip(x,y):
     print(a," : ",b)

print("--------------------------------------------")     
q=[]
e=[]
for a,b in zip(x,y):
     if b==maxCount:
          q.append(a)
for a,b in zip(x,y):
     if b==minCount:
          e.append(a)
if len(q)>0:                 
     print("Maxfrequency value :",end=" ")
     for i in q:
          print(i,end=" ")
     print()
     print("Minfrequency value :",end=" ")
     for i in e:
               print(i,end=" ")
else:
     print("Not valid data Found")               
