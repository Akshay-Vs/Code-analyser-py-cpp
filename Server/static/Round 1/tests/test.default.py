import sys
import emoji
from os import system
from platform import platform

sys.path.append("..")  # Adds higher directory to python modules path.
from problem import add


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def clear():
    if platform().startswith("Windows"):
        system("cls")
    else:
        system("clear")


pass_emoji = "✅"
fail_emoji = "❌"

test_set = [
    # test cases are defined here
    {"param_1": 0, "param_2": 0, "expected": 0},
    {"param_1": 0, "param_2": 1, "expected": 1},
    {"param_1": 1, "param_2": 1, "expected": 2},
    {"param_1": 1, "param_2": 2, "expected": 3},
    {"param_1": 1, "param_2": 3, "expected": 4},
    {"param_1": 1, "param_2": 4, "expected": 5},
    {"param_1": 1, "param_2": 5, "expected": 6},
    {"param_1": 1, "param_2": 6, "expected": 7},
    {"param_1": 1, "param_2": 7, "expected": 8},
    {"param_1": 1, "param_2": 8, "expected": 9},
    {"param_1": 1, "param_2": 9, "expected": 10},
]

clear()
print(colored(0, 100, 100, "Running tests..."))

for test_case in test_set:
    # unpack test case
    param_1 = test_case["param_1"]
    param_2 = test_case["param_2"]
    expected_output = test_case["expected"]

    output = add(param_1, param_2)  # test your function here

    if output != expected_output:
        print(
            colored(
                255,
                0,
                0,
                f"{fail_emoji} Test failed: add({param_1}, {param_2}) returned {output}, expected {expected_output}",
            )
        )
        sys.exit(1)
    else:
        print(
            colored(
                0,
                255,
                0,
                f"{pass_emoji} Test passed: add({param_1}, {param_2}) returned {output}",
            )
        )

print(
    colored(0, 100, 100, "-------------------\nCongragulations, You Passed all tests!")
)
