"""
input :
5
output :
3 2 4 5 1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = []
    for i in range(1, N + 1):
        nums.append(i)

    l = 0
    r = N - 1
    while True:
        print(nums[r])
        r -= 1
        if l > r: break

        print(nums[l])
        l += 1
        if l > r: break
