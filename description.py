import re

name_of_person = []
age_of_person = []
birthdate_of_person = []
description = input()
while description != 'make migrations':
    model = r'name is ([A-Z][a-z]+)\s([A-Z][a-z]+) \b(1[0-9]|[2-9][0-9]) years\b.*on (\d{2}-\d{2}-\d{4})\.'
    print(list(re.finditer(model, description)))
    description = input()
if not name_of_person:
    pass
else:
    for element in range(len(name_of_person)):
        print(f"Name of the person: {name_of_person[element]}.")
        print(f"Age of the person: {age_of_person[element]}.")
        print(f"Birthdate of the person: {birthdate_of_person[element]}")
