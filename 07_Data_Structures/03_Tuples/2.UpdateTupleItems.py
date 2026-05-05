# Define a tuple (tuples are immutable, so values cannot be changed directly)
programming = ("Python", "Java", "C#", "C++", "Javascript")

# Convert tuple to list (lists are mutable, so we can modify values)
x = list(programming)

# Change the value at index 1 ("Java" → "Go")
x[1] = "Go"

# Convert the list back to tuple
programming = tuple(x)

# Print the updated tuple
print("Updated Tuple:", programming)