import logging
import os

from aocd import submit as aoc_submit

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.ERROR)
LOG = logging.getLogger(__name__)


class AocUtil:
    def __init__(self, src_file, session_cookie=None):
        path = os.path.realpath(src_file)
        parts = path.split("/")
        self.part = parts[-1][:-3]
        self.day = int(parts[-2][1:])
        self.year = int(parts[-3][1:])
        self.src_dir = os.path.dirname(path)
        LOG.info(
            f"Initializing AoC {self.year} challenge day {self.day} part {self.part}"
        )

    def read_input(self):
        input_file = os.path.join(self.src_dir, "input.txt")
        LOG.info(f"Loading file {input_file}")

        with open(input_file) as f:
            input = f.read()
        return input[:-1]

    def submit(self, answer):
        aoc_submit(answer, part=self.part, day=self.day, year=self.year)

    @staticmethod
    def print_answer(answer):
        astr = str(answer)
        top = "*" * (len(astr) + 4)
        print(top)
        print(f"* {astr} *")
        print(top)


# def aoc_submit(answer, src_file):
#     parts = os.path.dirname().split('/')
#     print(f"Submitting solution for {parts}")
#     # submit()


# def read_input(src_file):
#     src_dir = os.path.dirname(os.path.realpath(src_file))
#     input_file = os.path.join(src_dir, "input.txt")

#     LOG.info(f"Loading file {input_file}")
#     with open(input_file) as f:
#         input = f.read()
#     return input[:-1]
