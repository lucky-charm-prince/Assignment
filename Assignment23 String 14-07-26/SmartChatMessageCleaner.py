# 3.  Smart Chat Message Cleaner

# A social media company noticed that users often enter messages with
# unnecessary spaces. To improve readability and storage efficiency, the
# system should remove extra spaces and keep only a single space between
# words.

# Input: Enter message: Java is easy

# Output: Cleaned Message: Java is easy

s = input("Enter the message: ")

s1 = ""
wordStarted = False

for i in range(len(s)):

    if s[i] != ' ':
        s1 += s[i]
        wordStarted = True

    elif wordStarted:
        if i + 1 < len(s) and s[i + 1] != ' ':
            s1 += ' '
            print(s1)

print("Cleaned Message:", s1)