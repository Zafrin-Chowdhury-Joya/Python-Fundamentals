# Define a dictionary (stores data in key-value pairs)
person = {
    "name": "Zafrin Chowdhury",
    "age": 0,
    "Gender": "Female",
    "language": "English",
    "country": "Bangladesh",
    "city": "Dhaka",
    "profession": "SQA",
    "email": "zafrin@gmail.com",
    "phone": "01300000000"
}

# -----------------------------------
# Remove key "name" and return its value
removed_value = person.pop("name")

# Print removed value
print("Removed value (name):", removed_value)

# Print updated dictionary
print("After removing name:", person)

# -----------------------------------
# Remove key "age" and return its value
removed_value2 = person.pop("age")

# Print removed value
print("Removed value (age):", removed_value2)

# Print updated dictionary
print("After removing age:", person)

# -----------------------------------
# Clear the dictionary (remove all key-value pairs)
person.clear()

# Print empty dictionary
print("After clear:", person)