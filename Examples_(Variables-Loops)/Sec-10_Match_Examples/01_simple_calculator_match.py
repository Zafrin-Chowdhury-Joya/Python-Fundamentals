def simple_calculator_match():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sign = input("Enter operator (+, -, *, /): ")

    match sign:
        case "+":
            print("Result:", a + b)
        case "-":
            print("Result:", a - b)
        case "*":
            print("Result:", a * b)
        case "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")
        case _:
            print("Invalid operator")

simple_calculator_match()