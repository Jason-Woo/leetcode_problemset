import sys

s = sys.stdin.readlines()
for line in s:
    ss = line.split()
    ans = 0
    for ele in ss:
        ans += int(ele)
    print(ans)