import requests
import os
import time
import zipfile
import io
import logging
import subprocess

from platform import platform


class TestSuite:
    def __init__(
        self,
        test_function: callable,
        test_cases: dict,
        url_endpoint: str,
        user_id: str,
        problem_id: int,
    ):
        self.test_function = test_function
        self.test_cases = test_cases
        self.pass_emoji = "✅"
        self.fail_emoji = "❌"
        self.warning_emoji = "⚠️"
        self.url_endpoint: str = url_endpoint
        self.user_id: str = user_id
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
    def colored(r: float, g: float, b: float, text: str):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    @staticmethod
    def clear():
        if platform().startswith("Windows"):
            os.system("cls")
        else:
            os.system("clear")

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
            "username": self.user_id,
            "problemId": self.problem_id,
            "time": time.time(),
            "status": "pass",
        }

        url_endpoint = self.url_endpoint + "/submit"
        res = requests.post(url_endpoint, json=payload)
        logging.info(f"Submitting to {url_endpoint}")
        logging.info(f"Payload: {payload}")
        logging.info(f"Response, POST Result: {res.status_code}")

    @staticmethod
    def is_last_problem(self):
        if self.problem_id < 0 or self.problem_id > 3:
            return True
        else:
            return False

    @staticmethod
    def next_problem(self):
        if self.is_last_problem(self):
            return print(
                self.colored(
                    0,
                    100,
                    100,
                    "\Congrats! You've completed all the tests\n",
                )
            )
        next_problem = self.problem_id + 1
        response = requests.get(self.url_endpoint + f"/problem/{next_problem}")

        if response.status_code == 200:
            logging.info("Proceeding to create next problem")
            timestamp = str(time.time())
            path = os.path.join(os.path.expanduser("~"), "BugBusters", timestamp)
            os.makedirs(path, exist_ok=True)
            z = zipfile.ZipFile(io.BytesIO(response.content))
            logging.info(f"Unzipping to {path}")
            z.extractall(path)
            logging.info("Successfully unzipped")
            logging.info(f"Opening next problem in VSCode")
            subprocess.run(["code", f"{path}/round_{next_problem}"])
        else:
            logging.error(
                f"Failed to get next problem, Status Code: {response.status_code}"
            )

    def unpack(self, test_case: dict):
        case_x = test_case["args"][0]
        case_y = test_case["args"][1]
        expected = test_case["expected"]
        logging.info(
            f"Unpacking: case_x: {case_x}, case_y: {case_y}, expected: {expected}"
        )
        return case_x, case_y, expected

    def run(self):
        # try:
            for test_case in self.test_cases:
                case_x, case_y, expected = self.unpack(test_case)
                output = self.test_function(case_x, case_y)

                if output == expected:
                    logging.info(f"Test passed: got {output}")
                    print(
                        self.colored(
                            0,
                            255,
                            0,
                            f"{self.pass_emoji}  Test passed: got {output}",
                        )
                    )

                else:
                    logging.error(f"Test failed: got {output}, expected {expected}")
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
            self.next_problem(self)

        # except Exception as e:
        #     logging.error(f"Test Suite Encountered an Error: {e}")
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
