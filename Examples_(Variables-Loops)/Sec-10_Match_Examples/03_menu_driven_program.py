while True:
    print("\nMenu:")
    print("1 → Add")
    print("2 → Subtract")
    print("3 → Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a + b)

        case 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a - b)

        case 3:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice, try again")