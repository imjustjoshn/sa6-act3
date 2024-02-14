def find_max(numbers, lamfunc):
    current_max = numbers[0]
    for num in numbers[1:]:
        if lamfunc(num, current_max) > 0:
            current_max = num
    return current_max

numbers = [5, 1, 9, 10, 2, 20, 6]
max_num = find_max(numbers, lambda x, y: x - y)
print(numbers)
print(f'Max: {max_num}')