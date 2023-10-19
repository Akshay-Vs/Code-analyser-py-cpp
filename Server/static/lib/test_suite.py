from os import system
from platform import platform


class TestSuite:
    def __init__(self, test_function: callable, test_cases: dict):
        self.test_function = test_function
        self.test_cases = test_cases
        self.pass_emoji = "✅"
        self.fail_emoji = "❌"
        self.warning_emoji = "⚠️"

        self.clear()
        print(
            self.colored(
                0,
                100,
                100,
                "--------------------------------------\nRunning Test Suite\n--------------------------------------",
            )
        )

    @staticmethod
    def colored(r, g, b, text: str):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    @staticmethod
    def clear():
        if platform().startswith("Windows"):
            system("cls")
        else:
            system("clear")

    @staticmethod
    def congratulate(self):
        print(
            self.colored(
                0,
                100,
                100,
                "--------------------------------------\nCongragulations, You Passed all tests!\n--------------------------------------",
            )
        )

        print(
            self.colored(
                0,
                100,
                100,
                "\nCheck file tree for your next challenge!\n",
            )
        )

    def unpack(self, test_case: dict):
        case_x = test_case["args"][0]
        case_y = test_case["args"][1]
        expected = test_case["expected"]

        return case_x, case_y, expected

    def run(self):
        try:
            for test_case in self.test_cases:
                case_x, case_y, expected = self.unpack(test_case)
                output = self.test_function(case_x, case_y)

                if output == expected:
                    print(
                        self.colored(
                            0,
                            255,
                            0,
                            f"{self.pass_emoji}  Test passed: ({case_x}, {case_y}) returned {output}",
                        )
                    )

                else:
                    return print(
                        self.colored(
                            255,
                            0,
                            0,
                            f"{self.fail_emoji}  Test failed: ({case_x}, {case_y}) returned {output}, expected {expected}, Try again!",
                        )
                    )
            self.congratulate(self)

        except Exception as e:
            print(
                self.colored(
                    255,
                    0,
                    0,
                    f"{self.warning_emoji} Test Suite Encountered an Error: {e}",
                )
            )
            return print(
                self.colored(
                    250,
                    250,
                    0,
                    f"\n___________________________________________________________\n\nIt's possible that the issue lies with the test suite.\n**Please reach out to the coordinators for assistance**.\nFeel free to try the test again!\n___________________________________________________________",
                )
            )


# Example usage
if __name__ == "__main__":

    def problem_function(x, y):  # this is the function you want to test
        return x + y

    test_set = [
        # test cases are defined here
        {"args": (1, 2), "expected": 3},
        {"args": (3, 4), "expected": 7},
        {"args": (5, 6), "expected": 1},
    ]

    test_suite = TestSuite(problem_function, test_set)  # create a test suite
    test_suite.run()  # run the test suite
