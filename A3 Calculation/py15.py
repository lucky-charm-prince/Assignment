distance1,time1=map(int,input("Enter the distace1 and time1 : ").split())

distance2,time2=map(int,input("Enter the distace2 and time2 : ").split())
speed1 =distance1/time1
speed2=distance2/time2
speed=int((speed1+speed2)/2)
print("Average speed is : ",speed)
