import sys
from test_suite import TestSuite

sys.path.append("..")
from problem import problem

test_set = [
    {
        "args": ([5, 2, 9, 3, 6], ),
        "expected": [2, 3, 5, 6, 9],
    },
    {
        "args": ([12, 11, 13, 5, 6], 5),
        "expected": [5, 6, 11, 12, 13],
    },
    {
        "args": ([7, 6, 5, 4, 3, 2, 1], 7),
        "expected": [1, 2, 3, 4, 5, 6, 7],
    },
    {
        "args": ([1], 1),
        "expected": [1],
    },
    {
        "args": ([9, 8, 7, 6, 5, 4, 3, 2, 1], 9),
        "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    },
]


test_suite = TestSuite(problem, test_set)
test_suite.run()
