# S = "Hello, world!" output:-"Hello world"

s = input("String : ")
s1 = ""

for i in s:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9') or i == ' ':
        s1 += i

print(s1)