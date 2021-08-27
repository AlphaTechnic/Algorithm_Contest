"""
input :

output :

"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

flag = False


def count_a_num(string):
    cnt = 0
    for digit in string:
        if digit == "a":
            cnt += 1
    return cnt


def count_b_num(string):
    cnt = 0
    for digit in string:
        if digit == "b":
            cnt += 1
    return cnt


def recur(string, target_string):
    global flag
    if len(string) > len(target_string):
        return
    if len(string) == len(target_string):
        if string == target_string:
            flag = True
        return
    if count_a_num(string) > count_a_num(target_string):
        return
    if count_b_num(string) > count_b_num(target_string):
        return

    recur(string + "a", target_string)
    recur("a" + string, target_string)

    cnt = count_a_num(string)
    string_refined = ""
    for _ in range(cnt):
        string_refined += "b"
    string_refined += string
    for _ in range(cnt):
        string_refined += "b"
    recur(string_refined, target_string)


def solution(v):
    global flag
    ans = []
    for target_string in v:
        flag = False
        recur("a", target_string)
        if flag:
            ans.append(True)
        else:
            ans.append(False)

    return ans


if __name__ == "__main__":
    v = ["abab", "bbaa", "bababa", "bbbabababbbaa"]
    print(solution(v))
