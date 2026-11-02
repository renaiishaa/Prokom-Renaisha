favorite_numbers = {
    'alya': [7, 10, 15],
    'bima': [12, 24],
    'citra': [5, 8, 20],
    'dina': [3, 9],
    'eka': [11, 17]
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print(number)