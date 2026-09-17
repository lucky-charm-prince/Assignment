# S = "the cat is on the mat" output : the: 2, is: 1 (theis)


s=input("String")
s1="the"
s2="is"

count1=0
count2=0
for i in range(len(s)-len(s1)+1):
    if s[i:i+len(s1)]==s1:
        count1+=1

for i in range(len(s)-len(s2)+1):
    if s[i:i+len(s2)]==s2:
        count2+=1
print(s1,count1)        
print(s2,count2)        
