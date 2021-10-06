"""
input :
3 2
9 5
1 2
3 10

output :
3 10
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    if N == 1 and K == 1:
        num = int(input())
        print(1, num)
        exit()

    tmp = []
    for i in range(1, N + 1):
        idx = [i for _ in range(K)]
        nums = list(map(int, input().rstrip().split()))
        zip(idx, nums)
        tmp += list(zip(idx, nums))
    deq = deque(tmp)

    while True:
        i, x = deq.popleft()
        x %= len(deq)
        deq.rotate(-x + 1)

        if len(deq) == 1:
            break

    print(deq[0][0], deq[0][1])
