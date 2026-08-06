def find_max(*arges):
    if not arges:
        return None
    max_value = arges[0]
    for number in arges:
        if number > max_value:
            max_value = number
    return max_value
result = find_max(3, 5, 7, 2, 8)
print(f"The maximum value is: {result}")

result = find_max()
print(f"The maximum value is: {result}")