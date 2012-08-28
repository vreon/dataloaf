"""
Data Loaf usage example: people generator
Builds a list of fake Westerosi and associated personal information.
"""
from __future__ import print_function
import json
import dataloaf as loaf

first_name = loaf.choice([
    loaf.choice('Aerys Bran Cleos Davos Eddard Farlen Gyles'.split()),
    loaf.choice('Alayne Brienne Catelyn Daenerys Elia Falyse Gilly'.split()),
])

last_name = loaf.choice(
    'Flowers Hill Pyke Rivers Sand Snow Stone Storm Waters'.split()
)

human_name = loaf.join(' ', [first_name, last_name])

pet_name = loaf.choice([
    'Ser Pounce', 'Lady Whiskers', 'Dog', 'Lady', 'Summer', 'Grey Wind',
    'Nymeria', 'Shaggydog', 'Ghost', 'Drogon', 'Viserion', 'Rhaegal'
])
pet_type = loaf.choice('cat dog direwolf raven dragon'.split())

pet = loaf.dict(
    name = pet_name,
    type = pet_type,
)

street_number = loaf.int(100, 9999)
street_name = loaf.choice(
    'North Iron River Wester Crown Reach Storm Dorne'.split()
)
street_type = loaf.choice('St. Ave. Rd. Way Lane'.split())
postal_code = loaf.int(10000, 99999)

address = loaf.list([
    loaf.join(' ', [
        loaf.transform(street_number, str),
        street_name,
        street_type
    ]),
    loaf.join(' ', [
        'Westeros, The Known World',
        loaf.transform(postal_code, str),
    ]),
])

person = loaf.dict(
    name = human_name,
    age = loaf.int(3, 90),
    pets = loaf.repeat(pet, loaf.int(0, 3)),
    address = address,
)

people = loaf.repeat(person, 3)

if __name__ == '__main__':
    print(json.dumps(people.bake(), indent=2))
