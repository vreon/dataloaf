"""
Data Loaf usage example: Goldblum generator
Generates alternate names by which you could address Jeff Goldblum, should you
ever encounter him removing his shoes at an airport. See also: Idle Thumbs 43
"""
from __future__ import print_function
import dataloaf as loaf

blum = loaf.choice(
    'jeff gold blum game cold fold gate blast cast cool coat'.split()
)

gold = loaf.transform(blum, lambda x: x.capitalize())

mc = loaf.weighted([
    (1, 'Mc'),
    (9, ''),
])

goldblum = loaf.weighted([
    (16, loaf.join('', [gold, ' ', mc, gold, blum])),
    (8, loaf.join('', [gold, blum, ' ', mc, gold, blum])),
    (1, loaf.join(' ', [gold] * 9)),
])

if __name__ == '__main__':
    print(goldblum.bake())
