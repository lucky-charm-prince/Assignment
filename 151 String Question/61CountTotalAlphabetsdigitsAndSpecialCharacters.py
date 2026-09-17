# S = "a1b!c2"  output:-  Alphabets: 3, Digits: 2, Special: 1

s=input("String : ")

alph=0
digi=0
spec=0
for i in s:
    if '0'<=i<='9':
        digi+=1
    elif 'a'<=i <='z' or    'A'<=i <='Z':
        alph+=1
    else:
        spec+=1
print("Alphabetes : ",alph)              
print("digi : ",digi)              
print("spec : ",spec)              
