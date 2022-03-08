ch2pos = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3),
    't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7),
    'o': (0, 8), 'p': (1, 0), 'a': (1, 1), 's': (1, 2),
    'd': (1, 3), 'f': (1, 4), 'g': (1, 5), 'h': (1, 6),
    'j': (1, 7), 'k': (1, 8), 'l': (2, 0), 'z': (2, 1),
    'x': (2, 2), 'c': (2, 3), 'v': (2, 4), 'b': (2, 5),
    'n': (2, 6), 'm': (2, 7),
}

MOD = 10 ** 9 + 7


def dist(ch1, ch2):
    x1, y1 = ch2pos[ch1]
    x2, y2 = ch2pos[ch2]
    return abs(x1 - x2) + abs(y1 - y2)


def get_dists(s):
    dists = []
    for i in range(len(s) - 1):
        dists.append(dist(s[i], s[i + 1]))
    return dists


def solution(s):
    dists = get_dists(s)

    tot = 0
    i = 1
    for val in dists:
        tot = (tot + (val * (i * (len(s) - i))) % MOD) % MOD
        i += 1

    return tot % MOD


if __name__ == "__main__":
    s = "tooth"
    solution(s)
