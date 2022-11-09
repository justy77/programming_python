# input:
work_hour = float(input("How many workhours this week?\n"))
salary = float(input("Your hourly salary?\n"))

overtime = 0
# over 40 hours is overtime
if work_hour - 40 > 0:
    overtime = work_hour - 40

# 50% increase to hourly wage:
overtime_salary = overtime * (salary * 1.5)
salary = (work_hour - overtime) * salary

# print and round result into 2 decimals:
print(f"Your weekly wage: {round(overtime_salary + salary, 2)}€")
