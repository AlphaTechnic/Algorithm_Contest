"""
input :
3 6 2
1 2 3

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K, C = map(int, input().rstrip().split())
    caps = list(map(int, input().rstrip().split()))

    for i in range(1, 6):
        tot = 0
        for cap in caps:
            tot += max(cap - i, 0)

        print(tot)
        if tot <= C:
             break
    print()
    print(i)
    print(tot)