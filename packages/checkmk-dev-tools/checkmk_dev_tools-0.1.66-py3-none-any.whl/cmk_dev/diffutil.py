#!/usr/bin/env python3

"""Does string search and replace on binary files, assuming 0-terminated strings

Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
conditions defined in the file COPYING, which is part of this source code package.
"""

import re
import sys
from functools import reduce
from pathlib import Path


def remove_noise(input_str: str) -> str:
    """Replace text components which make it hard to diff, e.g. timestamps
    and container IDs
    >>> print(remove_noise('''\\
    ...     2022-10-24 08:47:29,946 containers.py Container ID: 8a2a840eee
    ...     2022-10-24 08:47:29,946 execute in container 8a2a840eee: 'foo()'\\
    ... '''))
        <YYYY-MM-DDTHH:MM:SS,mmm> containers.py Container ID: <CONTAINER-ID>
        <YYYY-MM-DDTHH:MM:SS,mmm> execute in container <CONTAINER-ID>: 'foo()'
    """
    replacements = [
        (r"( \d{2}:\d{2}:\d{2} )", "<HH:MM:SS>"),
        (r"(\d{4}-\d{2}-\d{2}.\d{2}:\d{2}:\d{2}.\d{3})", "<YYYY-MM-DDTHH:MM:SS,mmm>"),
        (r"(/home/jenkins/workspace/.*/checkout)", "<WORKSPACE>/checkout"),
    ]

    def cleanup(line: str) -> str:
        if "Container ID: " in line:
            replacements.append((line[line.find("Container ID: ") + 14 :], "<CONTAINER-ID>"))
        return reduce(lambda s, p: re.sub(p[0], p[1], s), replacements, line)

    return "\n".join(map(cleanup, input_str.split("\n")))


def main():
    for path in map(Path, sys.argv[1:]):
        print(f"handle {path}")
        with path.open() as input_file:
            with (path.parent / f"{path.name}.cleaned").open("w") as output_file:
                output_file.write(remove_noise(input_file.read()))
                print(f"wrote {output_file.name}")


if __name__ == "__main__":
    main()
