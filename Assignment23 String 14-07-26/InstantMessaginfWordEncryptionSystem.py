# 4.  Instant Messaging Word Encryption System

# A messaging application wants to temporarily encrypt messages during
# transmission. The encryption rule is to reverse every word individually
# while keeping the word positions unchanged.

# Input: Enter message: java is powerful

# Output: Encrypted Message: avaj si lufrewop


s1=input("Enter the string : ")
s=s1+' '
i=0
start=0
s2=""


while i<len(s):
    if s[i]==' ':
        j=start
        count=0
        while j<i:
            s2+=s[i-count-1]
            count+=1
            j+=1

        s2+=' ' 
        
        
        
        start=i+1
    i+=1
print(s2)                       
