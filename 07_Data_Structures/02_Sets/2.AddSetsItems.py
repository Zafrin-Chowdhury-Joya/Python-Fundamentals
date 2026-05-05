# Define a set (sets are unordered and do not allow duplicate values)
programming = {"Python", "Java", "C#", "C++", "Javascript"}

# Add a single element to the set
programming.add("Go")
print("After add:", programming)

# Add multiple elements using update (list → set)
programming.update(["HTML", "PHP"])
print("After update:", programming)

# Sets do NOT allow duplicate values
# Adding "Python" again will NOT change the set
programming.add("Python")
print("After adding duplicate:", programming)