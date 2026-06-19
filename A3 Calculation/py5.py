hindi,english,math=map(int,input("Enter the marks of the hindi, english  & math : ").split(","))
print(f"Hindi : {hindi} \n English : {english} \n Math : {math}")
avg=(hindi+math+english)//3
print("Average of hindi , english , math is",avg)