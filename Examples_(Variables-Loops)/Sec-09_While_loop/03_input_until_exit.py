while True:
    user_input = input("Enter something (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Program stopped")
        break

    print("You entered:", user_input)