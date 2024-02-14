strings = ['grape', 'watermelon', 'banana', 'apple']
print(strings)

ordered_strings = sorted(strings, key=lambda x: (len(x), x))
print(ordered_strings)
