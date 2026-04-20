

correct_email = "zafrin@gmail.com"
correct_password = "admin123"

while True:
    user_email = input("Enter your email address: ")
    user_password = input("Enter your password: ")

    if user_email == correct_email and user_password == correct_password:
        print("Logged in successfully")
        break
    else:
        print("Invalid email or password. Try again.")