salary=int(input("Enter the salary: "))
working_days=int(input("Enter the number of working days: "))
working_hours=int(input("Enter the number of working hours: "))
salary_per_day=salary/working_days
salary_per_hour=salary_per_day/working_hours
print("Salary per day: ",salary_per_day)
print("Salary per hour: ",salary_per_hour)