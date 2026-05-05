# Define a set (sets are unordered and do not allow duplicates)
programming = {"Python", "Java", "C#", "C++", "Javascript"}

# Note: Sets do NOT support indexing, negative indexing, or slicing

# -----------------------------------
# Loop through each element in the set
for x in programming:
    # Print each item (order may vary because sets are unordered)
    print(x)

# -----------------------------------
# Check if an element exists in the set
if "Python" in programming:
    # If found, print the whole set
    print(programming)
else:
    # If not found, print message
    print("Not in set")