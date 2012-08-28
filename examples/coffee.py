"""
Data Loaf usage example: coffee
Generates preposterously complex Starbucks beverages.

This example relies heavily on the WeightedLoaf to (very) roughly approximate
the frequency of the various beverage components in actual orders.
"""
from __future__ import print_function
import dataloaf as loaf

drink = loaf.weighted([
    (8, 'latte'),
    (8, 'mocha'),
    (5, 'caramel macchiato'),
    (1, 'cappuccino'),
    (5, 'white mocha'),
    (2, 'americano'),
    (1, 'chai'),
])

size = loaf.weighted([
    (1, 'short'),
    (4, 'tall'),
    (10, 'grande'),
    (5, 'venti'),
 ])

shots = loaf.weighted([
    (1, 'single'),
    (7, 'double'),
    (10, 'triple'),
    (3, 'quad'),
    (1, '5-shot'),
 ])

decaf = loaf.weighted([
    (10, None),
    (5, 'decaf'),
    (2, 'half-decaf'),
    (1, '1/3 decaf'),
    (1, '2/3 decaf'),
 ])

temperature = loaf.choice(['extra hot', 'tepid', "kids' temperature"])

milk = loaf.weighted([ (6, 'nonfat'),
    (5, 'soy'),
    (2, 'breve'),
    (1, 'whole milk'),
    (1, '1%'),
 ])

syrup = loaf.choice([
    'vanilla', 'caramel', 'hazelnut', 'toffee nut', 'cinnamon dolce',
    'peppermint', 'raspberry', 'coconut',
 ])

quantity = loaf.choice('add no extra light'.split())

quantifiable = loaf.choice('foam whip sprinkles ice'.split())

sugar = loaf.choice(['one splenda', 'one sugar'])

modification = loaf.weighted([
    (4, loaf.join(' ', [quantity, quantifiable])),
    (1, temperature),
    (1, sugar),
    (1, 'drizzle'),
    (1, 'cinnamon powder'),
    (1, 'stirred'),
    (1, 'upside-down'),
])

# Most drinks don't have many modifications
modification_list = loaf.weighted([
    (1, loaf.join(' ', [modification] * 4)),
    (2, loaf.join(' ', [modification] * 3)),
    (10, loaf.join(' ', [modification] * 2)),
    (15, loaf.join(' ', [modification] * 1)),
    (10, None),
])

iced = loaf.choice(['iced', None])

coffee = loaf.join(' ', loaf.filter([
    iced, decaf, shots, size, syrup, milk, modification_list, drink
], lambda x: x is not None))

if __name__ == '__main__':
    print(coffee.bake())
