set1 = {"A", "B", "C", "D"}
set2 = {"C", "D", "E", "F"}

print(set1.union(set2))

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
set2.intersection_update(set1)
print(set2)