List = [1,2,3,4,5,6,7,8,9]

for item in List[:]:
    if item % 2 == 0:
        List.remove(item)

print("Remove Even Numbers from the List =",List)