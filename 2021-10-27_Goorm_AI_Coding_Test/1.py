"""
input :
3 3

output :
###
..#
###
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    bd = [['#' for _ in range(C)] for _ in range(R)]

    # set
    for r in range(1, R, 4):
        for c in range(C - 1):
            bd[r][c] = '.'
    for r in range(3, R, 4):
        for c in range(1, C):
            bd[r][c] = '.'

    # print
    for r in range(R):
        for c in range(C):
            print(bd[r][c], end='')
        print()
