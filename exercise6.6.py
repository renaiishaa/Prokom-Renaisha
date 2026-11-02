favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'sarah', 'mike', 'anna', 'phil', 'david']

for name in people:
    if name in favorite_languages.keys():
        print("Thank you, " + name.title() + ", for responding to the poll.")
    else:
        print(name.title() + ", please take the favorite languages poll.")