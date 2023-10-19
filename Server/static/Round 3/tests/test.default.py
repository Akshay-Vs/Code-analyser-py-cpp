import sys
from test_suite import TestSuite

sys.path.append("..")
from problem import add

test_set = [
    {"args": (1, 2), "expected": 3},
    {"args": (3, 4), "expected": 7},
    {"args": (5, 6), "expected": 11},
]

test_suite = TestSuite(add, test_set)
test_suite.run()
