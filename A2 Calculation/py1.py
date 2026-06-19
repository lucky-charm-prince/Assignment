

input_time = int(input("Enter time in seconds: "))
hour=input_time // 3600;
min=(input_time % 3600) // 60;
sec=input_time % 60;
print("Time in hour: ",hour)
print("Time in min: ",min)
print("Time in sec: ",sec)
