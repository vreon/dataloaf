"""
Data Loaf usage example: band names
Generates names for indie bands that are destined to languish in obscurity.
"""
from __future__ import print_function
import dataloaf as loaf

noun = loaf.choice((
    'killer man vomit machine sofa zombie horse door beef anger fire water '
    'house summer lip hammock stick robot wheel'
).split())

cap_noun = loaf.transform(noun, lambda x: x.capitalize())

uncountable_noun = loaf.choice(
    'Man Vomit Beef Anger Fire Water Summer'.split()
)

adjective = loaf.choice((
    'Cold Electric Sea Giant Nuclear Flaming Old Battle Damp DJ Summer Proto'
).split())

# This is a pretty gnarly example! It could probably be refactored.
band_name = loaf.weighted([
    (1, loaf.join('', ['The ', cap_noun, 's'])),
    (1, loaf.join('', ['The ', adjective, ' ', cap_noun, 's'])),
    (1, loaf.join('', ['The ', cap_noun, ' ', cap_noun, 's'])),
    (1, loaf.join('', [adjective, ' ', cap_noun])),
    (2, loaf.join('', [cap_noun, noun])),
    (2, loaf.join('', [cap_noun, ' ', cap_noun])),
    (1, loaf.join('', [cap_noun, ' ', cap_noun, 's'])),
    (1, loaf.join('', [cap_noun, 's of ', uncountable_noun]))
])

if __name__ == '__main__':
    print(band_name.bake())
