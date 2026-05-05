# Define a nested dictionary (dictionary inside another dictionary)
information = {
    "person": {   # First nested dictionary (personal information)
        "name": "Zafrin Chowdhury",
        "age": 0,
        "Gender": "Female",
        "language": "English",
        "country": "Bangladesh",
        "city": "Dhaka",
        "profession": "SQA",
        "email": "zafrin@gmail.com",
        "phone": "01300000000"
    },
    "education": {   # Second nested dictionary (academic results)
        "SSC": 4.68,
        "HSC": 4.18,
        "B.Sc": 3.87,
        "M.Sc": 3.87
    },
    "language": {   # Third nested dictionary (programming languages)
        "Python": "Python",
        "Java": "Java"
    }
}

# -----------------------------------
# Print the entire nested dictionary
print(information)

# -----------------------------------
# Access nested data using keys
# Access "name" from "person"
print("Name:", information["person"]["name"])

# Access "SSC" result from "education"
print("SSC GPA:", information["education"]["SSC"])