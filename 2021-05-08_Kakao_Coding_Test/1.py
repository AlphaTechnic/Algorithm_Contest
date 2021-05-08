"""
input :
1twothree45

output :
12345
"""

num_and_len = {
    'ze': ('0', 4),
    'on': ('1', 3),
    'tw': ('2', 3),
    'th': ('3', 5),
    'fo': ('4', 4),
    'fi': ('5', 4),
    'si': ('6', 3),
    'se': ('7', 5),
    'ei': ('8', 8),
    'ni': ('9', 4)
}

ans = ""
def solution(String):
    global ans
    i = 0
    while True:
        if i == len(String): break

        if ord('a') <= ord(String[i]) <= ord('z'):
            key = String[i] + String[i + 1]
            ans += num_and_len[key][0]
            i += num_and_len[key][1]
        else:
            ans += String[i]
            i += 1
    return ans


String = "1twothree45"
print(solution(String))
