from aocd.models import Puzzle
import webbrowser
import sys

year = int(sys.argv[1])
day = int(sys.argv[2])
p = Puzzle(year, day)

webbrowser.open_new(p.url)
