# Define a list (lists are mutable → can be modified)
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# Remove a specific element by value ("Python")
programming.remove("Python")
print("After remove:", programming)

# Remove element at index 2 ("C++")
programming.pop(2)
print("After pop index 2:", programming)

# Delete element at index 2 ("Javascript")
del programming[2]
print("After del index 2:", programming)

# Remove all elements from the list (empty the list)
programming.clear()
print("After clear:", programming)