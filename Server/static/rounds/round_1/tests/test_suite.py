import sys
import requests
import os
import json
import time
import zipfile
import io

from os import system
from platform import platform


class TestSuite:
    def __init__(
        self,
        test_function: callable,
        test_cases: dict,
        url_endpoint: str,
        device_id: str,
        problem_id: int,
    ):
        self.test_function = test_function
        self.test_cases = test_cases
        self.pass_emoji = "✅"
        self.fail_emoji = "❌"
        self.warning_emoji = "⚠️"
        self.url_endpoint: str = url_endpoint
        self.device_id: str = device_id
        self.problem_id: int = problem_id

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

    @staticmethod
    def submit(self):
        payload = {
            "deviceId": self.device_id,
            "problemId": self.problem_id,
            "time": time.time(),
            "status": "pass",
        }
        # print(payload)
        # print(self.url_endpoint)
        res = requests.post(self.url_endpoint, json=payload)
        # print(res.text)
        # print(res.status_code)

    @staticmethod
    def is_last_problem(self):
        if self.problem_id < 0 or self.problem_id > 3:
            return True
        else:
            return False

    @staticmethod
    def create_problem(self):
        pass

    @staticmethod
    def next_problem(self):
        if self.is_last_problem():
            return print(
                self.colored(
                    0,
                    100,
                    100,
                    "\Congrats! You've completed all the tests\n",
                )
            )
        next_problem = self.problem_id + 1
        response = requests.get(self.url_endpoint + f"/{next_problem}")

        if response.status_code == 200:
            path = os.path.join(os.path.expanduser("~"), "BugBusters")
            z = zipfile.ZipFile(io.BytesIO(response.content))
            z.extractall(path)
            os.system(f"cd {path} && code .")

    def unpack(self, test_case: dict):
        case_x = test_case["args"][0]
        case_y = test_case["args"][1]
        expected = test_case["expected"]

        return case_x, case_y, expected

    def run(self):
        # try:
        for test_case in self.test_cases:
            case_x, case_y, expected = self.unpack(test_case)
            output = self.test_function(case_x, case_y)

            if output == expected:
                print(
                    self.colored(
                        0,
                        255,
                        0,
                        f"{self.pass_emoji}  Test passed: got {output}",
                    )
                )

            else:
                return print(
                    self.colored(
                        255,
                        0,
                        0,
                        f"{self.fail_emoji}  Test failed: got {output}, expected {expected}, Try again!",
                    )
                )
        self.congratulate(self)
        self.submit(self)
        # self.next_problem(self)

    # except Exception as e:
    #     print(
    #         self.colored(
    #             255,
    #             0,
    #             0,
    #             f"{self.warning_emoji} Test Suite Encountered an Error: {e}",
    #         )
    #     )
    #     return print(
    #         self.colored(
    #             250,
    #             250,
    #             0,
    #             f"\n___________________________________________________________\n\nIt's possible that the issue lies with the test suite.\n**Please reach out to the coordinators for assistance**.\nFeel free to try the test again!\n___________________________________________________________",
    #         )
    #     )
