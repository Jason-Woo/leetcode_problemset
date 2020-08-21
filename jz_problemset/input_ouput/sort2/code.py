import sys

lines = sys.stdin.readlines()
for line in lines:
    print(' '.join(sorted(line)))