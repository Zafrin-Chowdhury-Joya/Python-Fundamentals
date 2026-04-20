age = int(input("Enter your age: "))
citizenship = input("Enter your city (Dhaka/Sylhet): ")

if citizenship == "Dhaka":
    if age >= 18:
        print("You are allowed to vote in Dhaka")
    else:
        print("You are not allowed to vote in Dhaka")

elif citizenship == "Sylhet":
    if age >= 18:
        print("You are allowed to vote in Sylhet")
    else:
        print("You are not allowed to vote in Sylhet")

else:
    print("You are not allowed to vote in Bangladesh")