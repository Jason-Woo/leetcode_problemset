import sys

s = sys.stdin.readlines()
for line in s:
    ans = 0
    ss = line.split()
    for i in range(1, len(ss)):
        ans += int(ss[i])
    print(ans)