"""
Parse and traverse a Data Loaf grammar.
"""
from __future__ import print_function
import argparse
import sys
from . import Grammar

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '--num', '-n', metavar='N', type=int, default=1,
    help='number of traversals to perform',
)
parser.add_argument(
    '--abort', '-a', metavar='N', type=int, default=0,
    help='abort a traversal after N iterations',
)

args = parser.parse_args()

gmr = Grammar(sys.stdin.read())
for i in range(args.num):
    print(gmr.walk(max_iterations=args.abort))
