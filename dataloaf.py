"""
Parse and traverse a Data Loaf grammar.
"""
from __future__ import print_function
import argparse
import random
import re
import sys

__version__ = '0.1.0'


# TODO: Make a WeightedMapping that caches sum
def random_weighted(list_):
    total = sum([x[0] for x in list_])
    n = random.uniform(0, total)
    for weight, item in list_:
        if n < weight:
            break
        n = n - weight
    return item


class Grammar(object):
    def __init__(self, string):
        self.parse(string)

    def parse(self, string):
        self.start = None
        self.rules = {}

        current_symbol = None
        rule_re = re.compile(r'^\s+(\d+)\s*(.*)$')

        for line in string.split('\n'):
            line = line.rstrip()

            if not len(line):
                continue

            match = rule_re.match(line)
            if match is None:
                self.start = self.start or line
                current_symbol = line
            else:
                self.rules.setdefault(current_symbol, []).append((
                    int(match.group(1)), match.group(2)
                ))

    def walk(self, max_iterations=None):
        result = random_weighted(self.rules[self.start])
        something_matched = True
        iterations = 0

        while something_matched and (
            not max_iterations or iterations < max_iterations
        ):
            something_matched = False
            for symbol in self.rules:
                result, num_matches = re.subn(
                    re.escape(symbol),
                    random_weighted(self.rules[symbol]),
                    result,
                    1,
                )
                if num_matches:
                    something_matched = True

        return result


def _cli(args):
    gmr = Grammar(sys.stdin.read())
    for i in range(args.num):
        print(gmr.walk(max_iterations=args.abort))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--num', '-n',
        metavar='N',
        type=int,
        default=1,
        help='number of traversals to perform',
    )
    parser.add_argument(
        '--abort', '-a',
        metavar='N',
        type=int,
        default=0,
        help='abort a traversal after N iterations',
    )

    _cli(parser.parse_args())
