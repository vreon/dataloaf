"""
Data Loaf usage example: Ghiscari names
Builds names that sound like Ghiscari characters from George R. R. Martin's
"A Song of Ice and Fire" novels.
"""
from __future__ import print_function
import dataloaf as loaf

start = loaf.choice('Gr Kr Pr Ozn Gh H N'.split())
vowel = loaf.choice('e a ah i y o'.split())
middle_consonant = loaf.choice('d l s z n zn nd'.split())
end_consonant = loaf.choice('d k l s r z n'.split())

middle = loaf.weighted([
    (1, ''),
    (2, loaf.join('', [vowel, middle_consonant])),
])
end = loaf.join('', [vowel, end_consonant])

name = loaf.join('', [start, middle, end])

zo = loaf.weighted([
    (3, 'zo'),
    (3, 'mo'),
    (1, 'na'),
])

full_name = loaf.join(' ', [name, zo, name])

if __name__ == '__main__':
    print(full_name.bake())
