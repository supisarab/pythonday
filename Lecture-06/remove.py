fruits_with_dulicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruits_with_dulicates:
    fruits_with_dulicates.remove("apple")
print(f"Fruits after remove: {fruits_with_dulicates}")