"""
input :
[[1, 4], [3, 4], [3, 10]]

output :
[1, 10]
"""

from collections import Counter


def solution(points):
    x_vals = []
    y_vals = []
    for x, y in points:
        x_vals.append(x)
        y_vals.append(y)

    ans_x = Counter(x_vals).most_common()[-1][0]
    ans_y = Counter(y_vals).most_common()[-1][0]
    return [ans_x, ans_y]


# points = [[4, 4], [5, 4], [4, 7]]
# print(solution(points))
