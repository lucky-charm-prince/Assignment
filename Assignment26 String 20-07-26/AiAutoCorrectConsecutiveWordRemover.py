# # 2. AI Auto-Correct Consecutive Word Remover

# An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

# The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

# ### Input:

# ```text
# hello hello hello team meeting meeting started
# ```

# ### Output:

# ```text
# hello team meeting started
# ```

# ---

s=input("Enter the String : ")
s1=""
word=s.split()
for i in word:
    if i not in s1:
        s1+=i+" "
print(s1)        