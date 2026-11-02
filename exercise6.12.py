pet1 = {
    'animal': 'cat',
    'owner': 'Alya',
    'food': 'fish',
    'age': 2
}

pet2 = {
    'animal': 'dog',
    'owner': 'Bima',
    'food': 'meat',
    'age': 3
}

pet3 = {
    'animal': 'rabbit',
    'owner': 'Citra',
    'food': 'carrot',
    'age': 1
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nAnimal:", pet['animal'].title())
    print("Owner:", pet['owner'])
    print("Favorite Food:", pet['food'].title())
    print("Age:", pet['age'], "years old")