
# Input:
# Total seconds = 7384

# Expected Output:
# Hours = 2
# Minutes = 3
# Seconds = 4


total_second=int(input("Total second : "))
hour=total_second//3600
min=(total_second%3600)//60
sec=total_second%60
print("Hours : ",hour  )
print("Min : ",min  )
print("Sec : ",sec  )