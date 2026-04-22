age = int(input("Enter an age : "))
if age > 0 :
    if age <= 5 :
        print("Free")
elif age >5 :
    if age <=18 :
        print("Discount")

elif age >=18 :
    if age >0 :
        print("Full price")

else :
    print ("Age is not correct ")