cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10600000,
        'fact': 'It is the capital city of Indonesia.'
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'It is one of the most populated cities in the world.'
    },
    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'It is known as the City of Light.'
    }
}

for city, information in cities.items():
    print("\nCity:", city.title())
    print("Country:", information['country'].title())
    print("Population:", information['population'])
    print("Fact:", information['fact'])