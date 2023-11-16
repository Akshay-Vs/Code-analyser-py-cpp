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


config: Config = Config()
config_data = config.read_config()
user_id = config_data["user_id"]
url_endpoint = config_data["url_endpoint"]
problem_id = 0

test_suite = TestSuite(
    add_two_numbers,
    test_set,
    url_endpoint,
    user_id,
    problem_id,
)

test_suite.run()  # run the test suite
