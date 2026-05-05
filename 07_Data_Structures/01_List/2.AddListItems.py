# Define a list (lists are mutable → can be changed)
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# Add an element at the end of the list
programming.append("Go")
print("After append:", programming)

# Insert an element at index 2 (3rd position)
programming.insert(2, "HTML")
print("After insert:", programming)

# Remove the last element from the list
programming.pop()
print("After pop:", programming)

# Define another list
newList = ["PHP", "HTML", "C++", "Javascript"]

# Add all elements of newList to programming list
programming.extend(newList)
print("After extend:", programming)