# S = "abc", n = 2  output: "ab, bc"

s=input("String")
n=int(input("String size : "))
for i in range(len(s)-n+1):
    print(s[i:i+n])
