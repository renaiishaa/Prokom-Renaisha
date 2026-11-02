pet1 = {
    'animal': 'cat',
    'owner': 'Alya'
}

pet2 = {
    'animal': 'dog',
    'owner': 'Bima'
}

pet3 = {
    'animal': 'rabbit',
    'owner': 'Citra'
}

pet4 = {
    'animal': 'bird',
    'owner': 'Dina'
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print("Animal:", pet['animal'])
    print("Owner:", pet['owner'])
    print()