def prime_numbers(n):
    if n>1 :
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number : "))
if prime_numbers(num):
    print("The prime number is prime")
else :
    print("The prime number is not prime")