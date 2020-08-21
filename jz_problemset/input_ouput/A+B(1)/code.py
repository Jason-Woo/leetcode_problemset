import sys
a = sys.stdin.readlines()
for line in a:
    s = line.split()
    print(int(s[0])+int(s[1]))