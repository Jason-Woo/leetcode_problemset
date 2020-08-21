import sys

while True:
    s = sys.stdin.readline()
    a = s.split()
    if a[0] == '0':
        break
    else:
        ans = 0
        for i in range(int(a[0])):
            ans += int(a[i + 1])
        print(ans)