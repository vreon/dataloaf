"""
Data Loaf usage example: video games
Generates titles for the next AAA blockbuster.
"""
from __future__ import print_function
import dataloaf as loaf

noun = loaf.choice((
    'Age Battle Call Colossus Company Chronicles Dawn Day Defeat Duty Empires '
    'Fortune Future Gears Heroes Honor League Legends Medal Men Origins '
    'Prince Soldier Shadow Star War World'
).split())

fantasy_noun = loaf.choice((
    'Age Battle Blade Champions Chronicles Curse Dark Darkness Dragon Eternal '
    'Fable Fire God Guild Heroes Knights Legend Lost Night Quest Shadow Tales '
    'Wonders Wrath'
).split())

title = loaf.choice([
    loaf.join(' ', [noun, 'of', noun]),
    loaf.join(' ', [fantasy_noun, fantasy_noun]),
    loaf.join(' ', [fantasy_noun, 'of the', fantasy_noun]),
])

game = loaf.choice([
    title,
    loaf.join(': ', [title, title]),
])

if __name__ == '__main__':
    print(game.bake())
