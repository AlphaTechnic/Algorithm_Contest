"""
input :
7 13
0 1 2 3 5 8 13

output :
3
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()
    nums_refined = list()

    ind = 0
    while True:
        a = nums[ind]
        if a >= K:
            nums_refined.append(a)
            ind += 1
            if ind == len(nums): break
            continue
        if ind == len(nums) - 1:
            if a >= K:
                nums_refined.append(a)
            break
        b = nums[ind + 1]
        nums_refined.append(a + b + K / 2)
        ind += 2
        if ind >= len(nums):
            break

    print(nums_refined)

    cnt = 0

    ind = 0
    tot = 0
    while True:
        tot += nums_refined[ind]
        if tot >= K:
            tot = 0
            cnt += 1
        ind += 1
        if ind == len(nums_refined):
            break

    print(cnt)