s=input("Enter the String : ")
n=int(input("Enter the index"))
if len(s)+1>=n and n>0:
    print(ord(s[n-1]))
    