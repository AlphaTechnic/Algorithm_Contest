import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

chk_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ','}


def solution(amountText):
    if amountText[0] == ',':
        return False
    if amountText[-1] == ',':
        return False

    for char in amountText:
        if char not in chk_set:
            return False

    ind = len(amountText) - 1
    cnt = 1
    while True:
        if cnt % 4 == 0:
            pass
        else:
            if amountText[ind] == ',':
                return False
        cnt += 1
        ind -= 1

        if ind == -1:
            break

    if amountText[0] == '0':
        ind = len(amountText) - 1
        cnt = 1
        while True:
            if cnt % 4 == 0:
                pass
            else:
                if amountText[ind] == ',' or amountText[ind] != '0':
                    return False
            cnt += 1
            ind -= 1

            if ind == -1:
                break

    return True


if __name__ == "__main__":
    print(solution("000"))
