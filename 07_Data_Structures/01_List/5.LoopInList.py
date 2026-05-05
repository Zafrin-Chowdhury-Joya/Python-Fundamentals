# Define a list
programming = ["Python", "Java", "C#", "C++", "Javascript"]

# -----------------------------------
# Loop 1: Direct iteration (for-each style)
for item in programming:
    # Print each element in the list
    print(item)

# -----------------------------------
# Loop 2: Index-based iteration
for i in range(0, len(programming)):
    # Print index and corresponding value
    print(f'Index {i} : {programming[i]}')

# -----------------------------------
# Loop 3: List comprehension (used here for printing)
# This creates a temporary list (not recommended just for printing)
[print(item) for item in programming]