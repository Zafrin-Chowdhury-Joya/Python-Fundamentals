from pandas.core.computation.expr import intersection

list1 = ["Python", "Java", "C#", "C++", "Javascript"]
list2 = ["PHP", "HTML", "C++", "Javascript"]
common = list(set(list1).intersection(set(list2)))

print("Common elements:", common)



