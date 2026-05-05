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

# Print the entire dictionary
print(person)

# Access and print specific values using keys
print("Gender =", person["Gender"])      # Access value of 'Gender'
print("Language =", person["language"])  # Access value of 'language'

# Get and print all keys from the dictionary
print("Keys =", person.keys())

# Get and print all values from the dictionary
print("Values =", person.values())

# Get and print all key-value pairs as tuples
print("Items =", person.items())