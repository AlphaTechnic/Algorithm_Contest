"""
input :

output :

"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

flag = False


def chk_b(string):
    idx = -1
    for i, ch in enumerate(string[0:len(string) // 2]):
        if ch == 'a':
            idx = i
            break

    if idx == -1:
        return -1
    return idx


def chk_a(string):
    cnt = 0
    for ch in string:
        if ch == 'a':
            cnt += 1
    return cnt


def recur(string):
    global flag
    if len(string) == 1:
        if string == 'a':
            flag = True
    if len(string) < 1:
        return

    if string[0] == string[-1] == 'b':
        b_num = chk_b(string)
        a_num = chk_a(string[b_num: -b_num])
        if a_num != b_num:
            return

        idx = 0
        for i, ch in enumerate(string):
            if ch == 'a':
                idx = i
                break
        recur(string[idx:-idx])
    elif string[-1] == 'a':
        recur(string[:-1])
    elif string[0] == 'a':
        recur(string[1:])


def solution(v):
    global flag
    ans = []
    for string in v:
        flag = False
        recur(string)
        if flag:
            ans.append(True)
        else:
            ans.append(False)

    return ans


if __name__ == "__main__":
    v = ["bb"]
    print(solution(v))
