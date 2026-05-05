# Define a tuple (tuples are immutable → cannot be changed)
programming = ("Python", "Java", "C#", "C++", "Javascript")

# Access element at index 2 (3rd element)
print(programming[2])   # Output: C#

# Access element using negative index (-3 → 3rd from end)
print(programming[-3])  # Output: C#

# Slice elements from index 2 to 3 (end index 4 is excluded)
print(programming[2:4]) # Output: ('C#', 'C++')