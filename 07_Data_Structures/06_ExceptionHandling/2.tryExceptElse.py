
try :
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except Exception as e:
    print("You cannot divide by zero.Error :",e)
else :
    print("The result is",result)
finally:
    print("The program is done.")