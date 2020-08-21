import sys
a = int(sys.stdin.readline())
for _ in range(a):
    ss = sys.stdin.readline()
    s = ss.split()
    print(int(s[0])+int(s[1]))