from collections import deque
import sys


def parser1(s_num):
    s_num = deque(list(s_num))
    interval = 1
    num = []
    try:
        while s_num:
            num.append([])
            for _ in range(interval):
                num[-1].append(s_num.popleft())
            if num[-1] == ['9']:
                interval += 1
            elif num[-1] == ['9', '9']:
                interval += 1
            elif num[-1] == ['9', '9', '9']:
                interval += 1
            if len(num) >= 2:
                a = int(''.join(num[-2]))
                b = int(''.join(num[-1]))
                if b - a != 1:
                    return None, None
        a = int(''.join(num[0]))
        b = int(''.join(num[-1]))
        return a, b
    except:
        return None, None


def parser2(s_num):
    #print(s_num)
    s_num = deque(list(s_num))
    interval = 2
    num = []
    try:
        while s_num:
            num.append([])
            for _ in range(interval):
                num[-1].append(s_num.popleft())
            if num[-1] == ['9', '9']:
                interval += 1
            elif num[-1] == ['9', '9', '9']:
                interval += 1
            if len(num) >= 2:
                a = int(''.join(num[-2]))
                b = int(''.join(num[-1]))
                if b - a != 1:
                    return None, None
        a = int(''.join(num[0]))
        b = int(''.join(num[-1]))
        return a, b
    except:
        return None, None


def parser3(s_num):
    s_num = deque(list(s_num))
    interval = 3
    num = []
    while s_num:
        num.append([])
        for _ in range(interval):
            num[-1].append(s_num.popleft())
        if num[-1] == ['9', '9', '9']:
            interval += 1
        if len(num) >= 2:
            a = int(''.join(num[-2]))
            b = int(''.join(num[-1]))
            if b - a != 1:
                return None, None
    a = int(''.join(num[0]))
    b = int(''.join(num[-1]))
    return a, b


def solution(s_num):
    functions = [parser1, parser2, parser3]
    for parser in functions:
        a, b = parser(s_num)
        if a is not None:
            return a, b


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")

    s_num = input()
    a, b = solution(s_num)
    print(a, b)