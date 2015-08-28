#!/usr/bin/env python

import sys
import re

bugre = re.compile("bug\\s+(\\d+)", re.I);

def searchFile(f, path):
    first = True
    section = ''

    for l in f.readlines():
        # Skip trailing/leading whitespace
        s = l.strip()

        # We don't care about top-level comments
        if len(s) < 2 or s[0] in ('#', ';'):
            continue

        if s[0] == '[' and s[-1] == ']':
            section = s[1:-1]
            continue
        if not s.startswith("skip-if"):
            continue

        reasons = s.split('=', 1)[1].strip()
        split = reasons.split('#', 1)

        comment = ""
        expr = split[0]
        if len(split) > 1:
            comment = split[1]

        if expr.find("e10s") == -1:
            continue

        bugno = bugre.search(comment)
        if section == "DEFAULT":
            if not bugno:
                print "=== %s - MISSING BUGNUM" % path
            else:
                print "=== %s - %s" % (path, bugno.group(1))
            break

        if first:
            first = False
            print "=== %s" % path

        if not bugno:
            print "%s - MISSING BUGNUM" % section
        else:
            print "%s - %s" % (section, bugno.group(1))

for path in sys.argv[1:]:
    with open(path) as f:
        searchFile(f, path)
