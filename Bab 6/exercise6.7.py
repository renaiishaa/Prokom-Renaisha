person1 = {
    'first_name': 'Alya',
    'last_name': 'Putri',
    'age': 19,
    'city': 'Surakarta'
}

person2 = {
    'first_name': 'Bima',
    'last_name': 'Pratama',
    'age': 20,
    'city': 'Jakarta'
}

person3 = {
    'first_name': 'Citra',
    'last_name': 'Lestari',
    'age': 18,
    'city': 'Yogyakarta'
}

people = [person1, person2, person3]

for person in people:
    print("\nFirst Name:", person['first_name'])
    print("Last Name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])