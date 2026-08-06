def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

print(is_armstrong_number(153))  
print(is_armstrong_number(9474))  
print(is_armstrong_number(123))  
