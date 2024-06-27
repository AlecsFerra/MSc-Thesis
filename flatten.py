#! /usr/bin/env python3

import os
import re

def flatten(root_dir, file_name):
    content = ""
    try:
        full_path = os.path.join(root_dir, file_name)
        with open(full_path, "r") as f:
            content = f.readlines()
    except:
        print(f"File '{full_path}' not found") # type: ignore

    def do_flatten(line):
        matched = re.match(r"\\(sub)?import{(.*)}{(.*)}", line)
        if matched:
            dir = matched.group(2)
            file = f"{matched.group(3)}.tex"
            return flatten(os.path.join(root_dir, dir), file)
        else:
            return line
    return ''.join(map(do_flatten, content)) # type: ignore

out = flatten(".", "thesis.tex")

with open("flat.tex", "w") as f:
    f.write(out)
