def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result =result * i
    return result
num = int(input("Enter a number for factorial : "))
print("Factorial:", factorial(num))