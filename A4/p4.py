
speed=int(input("Enter the speed : "))
hour=int(input("Enter the hour :  "))
min=int(input("Enter the minute :"))

total_time_min=min/60;
total_time=hour+total_time_min


print("Total time taken is : ",total_time," hours ")

distance=speed*total_time
print("Total distance travelled is : ",distance," km ")

