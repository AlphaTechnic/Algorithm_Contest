"""
input :
3 3
1 2 2
3 1 3
2 3 2
1 3

output :
3
"""
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

flag = False


def recur(nums, tar):
    global flag
    if len(nums) == len(tar):
        if set(nums) == set(tar):
            flag = True
        return
    if max(nums) > max(tar):
        return
    if min(nums) > min(tar):
        return

    p = [i for i in range(len(nums))]
    combis = list(combinations(p, 2))

    for a, b in combis:
        new_nums = []
        new_nums.append(nums[a] + nums[b])
        for i, num in enumerate(nums):
            if i != a and i != b:
                new_nums.append(num)
        recur(new_nums, tar)


def solution(p, q):
    global flag

    ans = []
    for i in range(len(p)):
        flag = False
        recur(p[i], q[i])
        if flag:
            ans.append(True)
        else:
            ans.append(False)
    return ans


if __name__ == "__main__":
    p = [[4, 3, 3], [1, 2, 3], [3, 2, 4]]
    q = [[5, 5], [5, 1], [1, 8]]
    print(solution(p, q))
