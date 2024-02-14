from functools import reduce

num1 = 15
num2 = 135
num3 = 1039

def find_sum(num):
    string = str(num)
    digits = list(string)
    digits = [int(x) for x in digits]
    total = reduce(lambda x, y: x + y, digits)
    return total

print(f'When the input is 15: {find_sum(num1)}')
print(f'When the input is 135: {find_sum(num2)}')
print(f'When the input is 1039: {find_sum(num3)}')

