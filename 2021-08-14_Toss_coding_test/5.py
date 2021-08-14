"""
input :
6
4 2 6 3 1 5

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 19
TREE = [0 for _ in range(2 * PIV)]


def update(ind, x):
    ind += PIV
    TREE[ind] = x

    while True:
        ind >>= 1
        if ind == 0: return
        TREE[ind] = max(TREE[2 * ind], TREE[2 * ind + 1])


def query(l, r):
    l += PIV; r += PIV
    ret = 0
    while l <= r :
        if l & 1:
            ret = max(ret, TREE[l])
            l += 1
        if not r & 1:
            ret = max(ret, TREE[r])
            r -= 1
        l >>= 1; r >>= 1;
    return ret


def solution(fruitWeights, k):
    # fruitWeights: [30 40 10 20 30]
    # k : 3
    chk_set = set()

    for i, num in enumerate(fruitWeights):
        update(i, num)

    l = 0
    while True:
        max_val = query(l, l + k - 1)
        chk_set.add(max_val)

        if l + k - 1 == len(fruitWeights) - 1:
            break
        l += 1

    ans = sorted(list(chk_set), reverse=True)
    return ans


if __name__ == "__main__":
    print(solution([30, 40, 10, 20, 30], 3))
