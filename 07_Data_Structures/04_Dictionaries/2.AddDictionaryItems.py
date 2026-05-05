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

# Add a new key-value pair ("university") to the dictionary
person["university"] = "University of Chicago"

# Print updated dictionary
print(person)

# Add another key ("lincense") with value None (no value assigned yet)
person["lincense"] = None

# Print updated dictionary
print(person)

# Add "Zipcode" only if it does NOT already exist
# If key exists, it will NOT overwrite the existing value
person.setdefault("Zipcode", "424")

# Print final dictionary
print(person)