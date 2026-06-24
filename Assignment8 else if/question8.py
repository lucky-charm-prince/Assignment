temperature=int(input("enter the temperature="))
if temperature<0:
    print("freezing")
elif temperature>=0 and temperature<=20:
    print("clod")
elif temperature>=21 and temperature<=35:
    print("warm")
else:
    print("hot")