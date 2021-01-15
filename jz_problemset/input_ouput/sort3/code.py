import sys
 
lines = sys.stdin.readlines()
for line in lines:
    s = list(line.strip().split(','))
    print(s)
    print(','.join(sorted(s)))