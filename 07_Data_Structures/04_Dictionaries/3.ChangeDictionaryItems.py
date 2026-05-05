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
# Update the value of an existing key ("language")
person["language"] = "Bangla"

# Print updated dictionary
print("After updating language:", person)

# Update multiple key-value pairs at once
# If keys exist → values will be updated
# If keys do not exist → new keys will be added
person.update({"city": "Dhaka", "profession": "Developer"})

# Print updated dictionary
print("After update():", person)