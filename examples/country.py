"""
Data Loaf usage example: country song lyrics
Generates horrible country songs. Steel guitar not included.
"""
from __future__ import print_function
import dataloaf as loaf

someone = loaf.weighted([
    (2, 'I'),
    (2, 'you'),
    (1, "y'all"),
    (1, 'we'),
 ])
cap_someone = loaf.transform(someone, lambda x: x.capitalize())
someones = loaf.choice('my your'.split())
and_but_so = loaf.choice('and but so'.split())
to_a_place = loaf.weighted([
    (1, 'on out to the pasture'),
    (2, 'on out to the field'),
    (3, loaf.join(' ', ['on out to', someones, 'ranch'])),
    (1, 'on out to the rodeo'),
    (1, 'to the general store'),
    (2, 'to the bar'),
    (1, 'to the honkytonk'),
    (1, 'to the hoedown'),
    (2, 'to the barn'),
    (1, "fishin'"),
])
adjective = loaf.weighted([
    (2, 'drunken'),
    (2, 'no-good'),
    (2, 'low-down'),
    (2, 'dirty'),
    (1, 'darned'),
    (1, "gol'darned"),
])
noun = loaf.weighted([
    (1, 'heart'),
    (1, 'tractor'),
    (3, 'truck'),
    (3, 'girlfriend'),
    (1, 'cattle'),
    (1, 'sheep'),
    (2, 'shotgun'),
    (2, 'beer'),
    (1, 'dog'),
    (1, 'baby'),
])
verb = loaf.weighted((
    (2, 'see'),
    (3, 'take'),
    (3, 'break'),
    (2, 'leave'),
    (1, 'sleep with'),
    (1, 'plow'),
))
verbed = loaf.weighted([
    (2, 'seen'),
    (3, 'took'),
    (3, 'broke'),
    (2, 'left'),
    (1, 'slept with'),
    (1, 'plowed'),
])
possibly_verbed = loaf.weighted([
    (2, verbed),
    (2, loaf.join(' ', ('done', verbed))),
    (1, loaf.join(' ', ("ain't never", verbed))),
])
some_stuff = loaf.weighted([
    (2, loaf.join(' ', [someones, noun])),
    (1, loaf.join(' ', [someones, adjective, noun])),
])
possibly_verbed_some_stuff = loaf.weighted([
    (3, loaf.join(' ', [verbed, some_stuff])),
    (3, loaf.join(' ', ['done', verbed, some_stuff])),
    (1, loaf.join(' ', ["ain't never", verbed, some_stuff])),
    (1, loaf.join(' ', ["ain't never", verbed, 'no', adjective, noun])),
])
was_about_to = loaf.choice([
    loaf.join('', ['thought ', someone, "'d"]),
    'were gonna',
])

eeee = loaf.join('', loaf.repeat('ee', loaf.int(1, 10)))
well_someone = loaf.choice([
    loaf.join('', ['W', eeee, 'll, ', someone]),
    cap_someone,
])

and_consequence = loaf.choice([
    loaf.join(' ', [and_but_so, someone, possibly_verbed_some_stuff]),
    loaf.join(' ', [and_but_so, someone, 'went', to_a_place]),
])

scenario = loaf.choice([
    loaf.join(' ', [well_someone, possibly_verbed_some_stuff]),
    loaf.join(' ', [well_someone, was_about_to, verb, some_stuff]),
])

continued_scenario = loaf.choice([
    and_consequence,
    loaf.join(' ', ['and', possibly_verbed, some_stuff]),
])

when_scenario = loaf.join(' ', ['When', someone, verbed, some_stuff])

consequence = loaf.weighted([
    (2, loaf.join(' ', [someone, verbed, some_stuff])),
    (1, loaf.join(' ', [someone, 'went', to_a_place])),
])

verse = loaf.weighted([
    (5, loaf.join('\n', [scenario, continued_scenario, and_consequence, and_consequence])),
    (2, loaf.join('\n', [when_scenario, consequence, and_consequence, and_consequence])),
    (1, loaf.join('\n', [scenario, continued_scenario])),
])

song = loaf.join('\n\n', loaf.repeat(verse, loaf.int(3, 8)))

if __name__ == '__main__':
    print(song.bake())
