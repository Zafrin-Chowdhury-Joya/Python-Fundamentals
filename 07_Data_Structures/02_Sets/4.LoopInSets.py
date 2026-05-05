# Define a set (unordered collection, no duplicates)
programming = {"Python", "Java", "C#", "C++", "Javascript"}

# Create a new empty set to store updated values
new_set = set()

# Loop through each element in the original set
for language in programming:
    # Check if the current element is "Python"
    if language == "Python":
        # Replace "Python" with "GO"
        new_set.add("GO")
    else:
        # Add the original element to the new set
        new_set.add(language)

# Print the updated set
print("Updated Set:", new_set)