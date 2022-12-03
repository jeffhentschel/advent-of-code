import logging
import os

LOG = logging.getLogger(__name__)


def read_input(src_file):
    src_dir = os.path.dirname(os.path.realpath(src_file))
    input_file = os.path.join(src_dir, "input.txt")

    LOG.info(f"Loading file {input_file}")
    with open(input_file) as f:
        input = f.read()
    return input
