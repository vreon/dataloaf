# Data Loaf

Data Loaf is a module that helps you generate dummy data using declaratively
constructed object templates (or Loaves). You can also think of it as a system
for randomly walking context-free grammars. It's what powers
<http://dataloaf.42nex.us>.

A Loaf is basically just a class that implements `bake()`. Data Loaf comes with
several of them that wrap native types, but it's trivial to add your own.

## Usage

```python
>>> d8 = dataloaf.int(1, 8)
>>> d8.bake()
5
```

Nothing `random.randint` can't do, right? But check this out:

```python
>>> name = dataloaf.join('', [
...     dataloaf.choice(['Gr', 'Kl', 'Ur']),
...     dataloaf.choice(['oz', 'ug', 'un']),
... ])
>>> hit_points = dataloaf.transform(d8, lambda x: x + 1)
>>> item = dataloaf.weighted([
...     (10, 'gold coin'),
...     (2, 'amulet'),
...     (1, 'mystical tome'),
... ])
>>> inventory = dataloaf.repeat(item, dataloaf.int(0, 3))
>>> orc = dataloaf.dict(name=name, hit_points=hit_points, inventory=inventory)
>>> orcs = dataloaf.repeat(orc, 3)
>>> orcs.bake()
[
  {
    'hit_points': 8,
    'inventory': ['amulet', 'gold coin', 'gold coin'],
    'name': 'Klun'
  },
  {
    'hit_points': 3,
    'inventory': ['gold coin', 'gold coin'],
    'name': 'Uroz'
  }, 
  {
    'hit_points': 2,
    'inventory': ['mystical tome', 'gold coin'],
    'name': 'Klug'
  }
]
```

When a Loaf is baked, the `bake()` call propagates down the structure; objects
that don't respond to `bake()` are returned as-is. Note that you can also call
`bake()` on any of these intermediate loaves (e.g. `hit_points.bake()`), which
can be handy for debugging.

See the included examples or the documentation for further information.

## License

Data Loaf is made available under the terms of the Expat/MIT license (see
LICENSE.)
