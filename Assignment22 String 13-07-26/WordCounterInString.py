
# 3.
# Word Counter in Complaint Message

# A customer care system wants to count how many words are present in a complaint message.

# Input:
# Enter complaint: Delivery was delayed again today

# Output:
# Total words: 5

s=input("Enter the String : ").lower()
count=0

for i in range(2,len(s)):
    if (s[i]==' ' and 97<=ord(s[i-1])<=122):
        count+=1
    

if 'a'<=s[len(s)-1]<='z': 
    count+=1
print("Total word are : ",count)    

