# 2.
# Space Counter in Chat Messages

# A chat application wants to calculate how many spaces are used in a message.

# Input: Enter chat message: Good morning everyone how are you

# Output: Total spaces: 5


s=input("Enter the Sgtring ")
count=0
for i in s:
    if i==' ':
        count+=1
print("Total Spaces are :- ",count)        