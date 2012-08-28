"""
Data Loaf usage example: silly names
Generates ridiculous names that sound vaguely like "Bleff Jorgenson".
"""
from __future__ import print_function
import dataloaf as loaf

first_name = loaf.join('', [
    loaf.choice('Ch Bl Fl J'.split()),
    loaf.choice('e o a'.split()),
    loaf.choice('ff b g d rg sk rge n'.split()),
])

last_name = loaf.join('', [
    loaf.choice('Ja Jo Bla Gla De Sti'.split()),
    loaf.choice('ngle r bble ps ddings'.split()),
    loaf.choice('blab frob fran blerg stein rton'.split()),
])

name = loaf.join(' ', [first_name, last_name])

if __name__ == '__main__':
    print(name.bake())
