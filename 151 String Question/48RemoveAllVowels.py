# S = "aeiou XYZ"  output :- " XYZ"

s=input("String : ")
s1=""
for i in s:
    if i not in ['a','e','i','o','u']:
        s1+=i
print(s1)        