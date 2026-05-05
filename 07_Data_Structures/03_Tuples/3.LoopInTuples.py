# Define a tuple (tuples are immutable, so values cannot be changed directly)
programming = ("Python", "Java", "C#", "C++", "Javascript")

# Loop through each element directly (for-each style)
for x in programming:
    # Print each item in the tuple
    print(x)

# Loop using index (0 to length-1)
for i in range(len(programming)):
    # Access element using index and print it
    print(programming[i])