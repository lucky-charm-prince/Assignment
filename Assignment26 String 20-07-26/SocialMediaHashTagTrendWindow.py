# # 5. Social Media Hashtag Trend Window

# A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

# ### Input:

# ```text
# aabcbcdbca
# ```

# ### Output:

# ```text
# dbca
# ```

# ### Explanation:

# `dbca` contains all unique characters: a,b,c,d

# ---

s=input("Enter the String : ")
s1=""
for i in range(len(s)):
    s2=""
    for j in range(i,len(s)):
        if s[j] in s2:
            break
        s2+=s[j]
    if len(s2)>len(s1):
        s1=s2    
print(s1)        