# Define first list
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# Define second list
newList = ["PHP", "HTML", "C++", "Javascript"]

# -----------------------------------
# Join using extend (adds all elements of newList to programming)
programming.extend(newList)
print("After extend:", programming)

# -----------------------------------
# Join using append (duplicate elements safely)
# Use .copy() to avoid modifying list during iteration
for x in programming.copy():
    # Append each element again → duplicates the list
    programming.append(x)

print("After append loop:", programming)