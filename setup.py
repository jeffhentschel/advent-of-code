from aocd.models import Puzzle
import webbrowser
import sys

year = int(sys.argv[1])
day = int(sys.argv[2])
p = Puzzle(year, day)

print(p.easter_eggs)

with open(f"y{year}/d{day}/example.txt", "w") as f:
    f.write(p.example_data)

webbrowser.open_new(p.url)
