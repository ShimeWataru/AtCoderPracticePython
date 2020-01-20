import os
import sys
import pathlib


path = './cheatsheet.md'
path_w = './cheatsheet_new.md'
new_lines = []

print(path)

with open(path) as f:
    count = 0
    for s_line in f:
        new_line = s_line
        if s_line == "```\n":
            count += 1
            if count % 2 == 1:
                new_line = "```python\n"
            new_lines.append(new_line)
        else:
            new_lines.append(new_line)

with open(path_w, mode='w') as f:
    f.write("".join(new_lines))
