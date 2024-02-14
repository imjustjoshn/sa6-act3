#Test 1
n = 2
numbers = [1, 2, 3, 4, 5]
print(f'numbers = {numbers}')

new_list = list(map(lambda x: x ** n, numbers))
print(f'n = {n}')
print(new_list)

#Test 2
n2 = 4
numbers = [1, 2, 3, 4, 5]

new_list2 = list(map(lambda x: x ** n2, numbers))
print(f'n = {n2}')
print(new_list2)