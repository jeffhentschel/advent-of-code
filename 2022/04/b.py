import logging
import math
import os
import re
from pprint import pprint

from aoc.input import read_input

LOG = logging.getLogger(__name__)
input = read_input(__file__)

total = 0
for line in input.split('\n'):
    result = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line)
    e1s,e1e,e2s,e2e = map(int, result.groups())
    
    if e1s <= e2e and e1e >= e2s \
        or e2s <= e1e and e2e >= e1s:
        total +=1

print(total)
