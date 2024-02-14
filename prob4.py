list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

intersect_list = list(filter(lambda x: x in list1, list2))

print(list1)
print(list2)
print(intersect_list)
