import sys
from math import lcm


def cirle_path(n, m):
    if m == 1:
        return None
    print(*((x % n + 1) for x in range(0, (lcm(n, m - 1)), (m - 1))), sep='')


n = int(sys.argv[1])
m = int(sys.argv[2])
cirle_path(n, m)
