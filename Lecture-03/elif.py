num_employees = int(input("Enter the number of employees: "))
if num_employees < 50:
    print("This is small company.")
elif num_employees < 250:
    print("This is a medium company.")
elif num_employees >= 250:
    print("This is a large company.")