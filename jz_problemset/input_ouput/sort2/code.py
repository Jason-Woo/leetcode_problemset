import sys

lines = sys.stdin.readlines()
for line in lines:
    s = line.split()
    print(' '.join(sorted(s)))