# Define two sets
set1 = {"Python", "Java", "C#", "C++", "Javascript"}
set2 = {"Go", "HTML", "CSS", "Javascript"}

# -------------------------------
# Union Operation (Join both sets, remove duplicates)
joined_set = set1.union(set2)
print("Union (All unique elements):", joined_set)

# -------------------------------
# Intersection Operation (Common elements in both sets)
joined_set2 = set1.intersection(set2)
print("Intersection (Common elements):", joined_set2)

# -------------------------------
# Difference Operation (Elements in set1 but NOT in set2)
different_set = set1.difference(set2)
print("Difference (set1 - set2):", different_set)