hr_work = int(input("Enter the number of hours worked: "))
hr_rate = float(input("Enter the hourly rate: "))
if hr_work <= 40:
    gross_pay = hr_work * hr_rate
else:
    overtime_hours = hr_work - 40
    gross_pay = (40 * hr_rate) + (overtime_hours * hr_rate * 1.5)
    
print("Gross pay: $", format(gross_pay, '.2f'))