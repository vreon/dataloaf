import random


def _bake(thing):
    return thing.bake() if hasattr(thing, 'bake') else thing


class Loaf(object):
    pass


class IntLoaf(Loaf):
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def bake(self):
        return random.randint(self.lower, self.upper)


class JoinLoaf(Loaf):
    def __init__(self, joiner, parts):
        self.joiner = joiner
        self.parts = parts

    def bake(self):
        return _bake(self.joiner).join([_bake(p) for p in _bake(self.parts)])


class ChoiceLoaf(Loaf):
    def __init__(self, choices):
        self.choices = choices

    def bake(self):
        return _bake(random.choice(_bake(self.choices)))


class WeightedLoaf(Loaf):
    def __init__(self, choices):
        self.choices = choices
        self.total = sum([item[0] for item in choices])

    def bake(self):
        n = random.uniform(0, self.total)
        for weight, value in self.choices:
            if n < weight:
                break
            n = n - weight
        return _bake(value)


class DictLoaf(Loaf):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def bake(self):
        baked = {}
        for k, v in self.kwargs.items():
            baked[k] = _bake(v)
        return baked


class ListLoaf(Loaf):
    def __init__(self, items):
        self.items = items

    def bake(self):
        return [_bake(i) for i in self.items]


class RepeatLoaf(Loaf):
    def __init__(self, item, length):
        self.item = item
        self.length = length

    def bake(self):
        return [_bake(self.item) for i in range(_bake(self.length))]


class BakedObject(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ObjectLoaf(Loaf):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def bake(self):
        baked = {}
        for k, v in self.kwargs.items():
            baked[k] = _bake[v]
        return BakedObject(**baked)


class TransformLoaf(Loaf):
    def __init__(self, value, transformation):
        self.value = value
        self.transformation = transformation

    def bake(self):
        return self.transformation(_bake(self.value))


class FilterLoaf(Loaf):
    def __init__(self, values, filter):
        self.values = values
        self.filter = filter

    def __iter__(self):
        for v in self.values:
            baked = _bake(v)
            if self.filter(baked):
                yield baked

    def bake(self):
        baked = [_bake(v) for v in _bake(self.values)]
        return [b for b in baked if self.filter(b)]
