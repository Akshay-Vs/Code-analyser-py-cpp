from test_suite import TestSuite
from config_handler import Config

from importlib import util
from ctypes import c_int, cdll
from platform import platform
from argparse import ArgumentParser

import subprocess
import sys
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    filename="app.log",
    level=logging.INFO,
)  # logging configuration

# handling command line arguments
parser = ArgumentParser()
parser.add_argument("path", type=str, help="path to problem file")
parser.add_argument("language", type=str, help="language of problem file (c, py)")
args = parser.parse_args()

# handling problem file
problem_path = args.path
problem_language = args.language
logging.info(f"problem_path: {problem_path}, problem_language: {problem_language}")

if problem_language == "python":
    logging.info("Selected Language: Python")
    spec = util.spec_from_file_location("problem", problem_path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    problem = module.problem
    logging.info("Successfully loaded problem")

elif problem_language == "c":
    logging.info("Selected Language: C")
    subprocess.run(["gcc", "-shared", "-o", "problem.dll", problem_path])
    logging.info("Successfully compiled problem")

    if platform().startswith("Windows"):
        logging.info("Platform: Windows")
        lib = cdll.LoadLibrary(".\problem.dll")
        logging.info("Successfully loaded problem")
    else:
        logging.info("Platform: UNIX")
        lib = cdll.LoadLibrary("./problem.dll")
        logging.info("Successfully loaded problem")

    lib.main.argtypes = [c_int, c_int]
    lib.main.restype = c_int

    problem = lambda a, b: lib.main(a, b)

else:
    logging.error("Language not supported")
    sys.exit()


# region Test Instantiation
test_set = [
    {"args": [1, 2], "expected": 3},
    {"args": [3, 4], "expected": 7},
    {"args": [5, 6], "expected": 11},
]

logging.info("Successfully loaded test set")

config: Config = Config()
config_data = config.read_config()
user_id = config_data["user_id"]
url_endpoint = config_data["url_endpoint"]
problem_id = 2
logging.info("Successfully loaded config")

test_suite = TestSuite(
    problem,
    test_set,
    url_endpoint,
    user_id,
    problem_id,
)
logging.info("Successfully loaded test suite")
logging.info("Running test suite")
test_suite.run()  # run the test suite
# endregion
