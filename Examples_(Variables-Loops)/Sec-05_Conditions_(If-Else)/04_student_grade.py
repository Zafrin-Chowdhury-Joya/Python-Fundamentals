result = int(input("Enter the marks :"))
if result >= 90 and result <= 100 :
    print ("Grade is A")
elif result >= 75 and result <= 89 :
    print ("Grade is B")
elif result >= 50 and result <= 74 :
    print ("Grade is C")
elif result < 50 :
    print ("Fail")
else :
    print ("marks is not correct")