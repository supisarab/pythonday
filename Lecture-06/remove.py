fruits_with_dulicate = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruits_with_dulicate:
    fruits_with_dulicate.remove("apple")
print(f"Fruits after removr: {fruits_with_dulicate}")