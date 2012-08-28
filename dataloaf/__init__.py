"""
Data Loaf is a tool for generating randomized data structures using a
context-free grammar.
"""
from .loaf import (
    IntLoaf, JoinLoaf, ChoiceLoaf, WeightedLoaf, DictLoaf, RepeatLoaf,
    ObjectLoaf, TransformLoaf, FilterLoaf, ListLoaf
)

__version__ = '0.1.0'

# Convenience aliases
# This is kind of terrible
dict = DictLoaf
int = IntLoaf
object = ObjectLoaf
list = ListLoaf
choice = ChoiceLoaf
weighted = WeightedLoaf
repeat = RepeatLoaf
join = JoinLoaf
transform = TransformLoaf
filter = FilterLoaf
