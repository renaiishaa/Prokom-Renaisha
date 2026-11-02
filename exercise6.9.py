favorite_places = {
    'alya': ['bali', 'bandung', 'jogja'],
    'bima': ['tokyo', 'seoul'],
    'citra': ['paris', 'switzerland', 'bali']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("- " + place.title())