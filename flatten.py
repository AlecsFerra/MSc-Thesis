#! /usr/bin/env python3

import os
import re
import argparse

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
        
        return line

    return ''.join(map(do_flatten, content)) # type: ignore

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="flatten.py",
        description="Tranform a latex project that uses the '\\(sub)import' in"
            " a standalone latex file"
    )

    parser.add_argument(
        "source", 
        help="The main file of the latex project",
    )

    parser.add_argument(
        "output", 
        help="The name of the file used as output"
    )

    args = parser.parse_args()

    out = flatten(".", args.source)

    with open(args.output, "w") as f:
        f.write(out)
