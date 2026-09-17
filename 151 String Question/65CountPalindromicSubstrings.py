# S = "aaa"  output :-  6 (a, a, a, aa, aa, aaa)

s=input("String : ")

count=0

for i in range(0,len(s) ):
    for j in range(i,len(s) ):
        x=s[i:j+1]
        y=x[::-1]
        if x==y:
            count+=1
print(count)            