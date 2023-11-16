import json
from test_suite import TestSuite
from config_handler import Config

import os
import sys

test_set = [
    {"args": [1, 2], "expected": 3},
    {"args": [3, 4], "expected": 7},
    {"args": [5, 6], "expected": 11},
]
# Test Suite Usage
sys.path.append("..")
from problem import add_two_numbers

url_endpoint = "http://localhost:5000/submit"
device_id = "test_device_id"
problem_id = 0


config: Config = Config()
test_suite = TestSuite(
    add_two_numbers,
    test_set,
    url_endpoint,
    device_id,
    problem_id,
)

test_suite.run()  # run the test suite
