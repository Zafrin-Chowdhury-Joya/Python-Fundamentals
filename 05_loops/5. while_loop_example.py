correct_email = "zafrin@gmail.com"
correct_password = "admin123"

attempt = 0

while attempt < 3:
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == correct_email and password == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid credentials")
        attempt += 1

if attempt == 3:
    print("Account locked after 3 failed attempts")