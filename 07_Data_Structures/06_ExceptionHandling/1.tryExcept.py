
try :
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print(result)
except Exception as e:
    print("You cannot divide by zero.Error :",e)

