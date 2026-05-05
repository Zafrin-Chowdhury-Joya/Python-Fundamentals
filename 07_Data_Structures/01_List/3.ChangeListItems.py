# Define a list (lists are mutable → values can be changed)
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# Change the value at index 1 ("Java" → "Go")
programming[1] = "Go"
print("After updating index 1:", programming)

# Replace elements from index 2 to 3 (slice 2:4 → excludes index 4)
# "C#" and "C++" are replaced with "PHP" and "HTML"
programming[2:4] = ["PHP", "HTML"]
print("After slicing replacement:", programming)