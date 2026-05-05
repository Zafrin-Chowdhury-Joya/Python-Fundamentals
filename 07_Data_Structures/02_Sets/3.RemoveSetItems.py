# Define a set (unordered collection, no duplicates)
programming = {"Python", "Java", "C#", "C++", "Javascript"}

# Remove a specific element from the set
# If the element does not exist → raises KeyError
programming.remove("Javascript")
print("After remove:", programming)

# Discard an element from the set
# Does NOT raise error if element is not present
programming.discard("Javascript")
print("After discard:", programming)

# Remove and return a random element from the set
# (since sets are unordered, we don’t know which item will be removed)
removed_item = programming.pop()
print("Removed item:", removed_item)
print("After pop:", programming)

# -----------------------------------
# Clear the set (remove all elements)
programming.clear()
print("After clear:", programming)