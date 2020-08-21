import sys

s = sys.stdin.readline()
for _ in range(int(s)):
    a = sys.stdin.readline().split()
    ans = 0
    for i in range(1, len(a)):
        ans += int(a[i])
    print(ans)