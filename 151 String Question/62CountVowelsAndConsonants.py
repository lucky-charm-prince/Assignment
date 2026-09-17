# S = "apple" Vowels: 2, Consonants: 3

s=input("String : ")
vow=0
con=0

for i in s :
    if i in ['a','e','i','o','u']:
        vow+=1
    else:
        con+=1
print("Vowels : ",vow)            
print("Consonants : ",con)            
