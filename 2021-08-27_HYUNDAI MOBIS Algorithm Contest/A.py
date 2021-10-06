"""
input :

output :

"""

import sys
from itertools import permutations

input = sys.stdin.readline

chk = [False for _ in range(10000)]


def gen_num(order):
    N = len(order)

    if N == 1:
        for num in order[0]:
            if num == 0:
                continue
            chk[num] = True

    elif N == 2:
        digits = ""
        for num1 in order[0]:
            if len(digits) == 0 and num1 == 0:
                continue
            digits += str(num1)
            for num2 in order[1]:
                if len(digits) == 0 and num2 == 0:
                    continue
                digits += str(num2)
                chk[int(digits)] = True
                digits = digits[:-1]
            digits = ""

    elif N == 3:
        digits = ""
        for num1 in order[0]:
            if len(digits) == 0 and num1 == 0:
                continue
            digits += str(num1)
            for num2 in order[1]:
                if len(digits) == 0 and num2 == 0:
                    continue
                digits += str(num2)
                for num3 in order[2]:
                    if len(digits) == 0 and num3 == 0:
                        continue
                    digits += str(num3)
                    chk[int(digits)] = True
                    digits = digits[:-1]
                digits = digits[:-1]
            digits = ""

    elif N == 4:
        digits = ""
        for num1 in order[0]:
            if len(digits) == 0 and num1 == 0:
                continue
            digits += str(num1)
            for num2 in order[1]:
                if len(digits) == 0 and num2 == 0:
                    continue
                digits += str(num2)
                for num3 in order[2]:
                    if len(digits) == 0 and num3 == 0:
                        continue
                    digits += str(num3)
                    for num4 in order[3]:
                        if len(digits) == 0 and num4 == 0:
                            continue
                        digits += str(num4)
                        chk[int(digits)] = True
                        digits = digits[:-1]
                    digits = digits[:-1]
                digits = digits[:-1]
            digits = ""


def solution(v):
    arr_refined = []
    N = len(v)
    for vec in v:
        vec_refined = sorted(list(set(vec)))
        arr_refined.append(vec_refined)

    p = [i for i in range(N)]
    permu = list(permutations(p))

    for seq in permu:
        order = []
        for i in range(N):
            order.append(arr_refined[seq[i]])
            gen_num(order)

    ans = 1
    for i in range(1, 10000):
        if not chk[i]:
            ans = i
            break
    return ans


if __name__ == "__main__":
    v = [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]
    print(solution(v))
