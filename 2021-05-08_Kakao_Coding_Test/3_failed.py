"""
input :
["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

output :
"OOOOXOOO"
"""


def solution(N, K, cmds):
    LIST = ['_'] + [[i, True] for i in range(1, N+1)]
    IND = K
    st = []

    for cmd in cmds:
        if cmd[0] == "U":
            delta = int(cmd[-1])
            recent = IND
            i = IND - 1
            while True:
                if delta == 0 or i <= 1:
                    if i <= 1:
                        IND = i
                    else:
                        IND = recent
                    break
                if LIST[i][1] == False:
                    i = i - 1
                else:
                    recent = i
                    i = i - 1
                    delta -= 1


        elif cmd[0] == "D":
            delta = int(cmd[-1])
            recent = IND
            i = IND + 1
            while True:
                if delta == 0 or i == len(LIST)-1:
                    if i == len(LIST) - 1:
                        IND = i
                    else:
                        IND = recent
                    break
                if LIST[i][1] == False:
                    i = i + 1
                else:
                    recent = i
                    i = i + 1
                    delta -= 1

        elif cmd[0] == "C":
            LIST[IND][1] = False
            st.append(IND)
            recent = IND
            IND = IND + 1
            while True:
                if LIST[IND][1] == True or IND == len(LIST) - 1:
                    if IND == len(LIST) - 1:
                        IND = recent
                    else:

                    break

            IND = min(len(LIST) - 1, IND + 1)
        elif cmd[0] == "Z":
            restore = st.pop()
            LIST[restore][1] = True

    ans = ""
    for i, TorF in LIST[1:]:
        if TorF == True:
            ans += "O"
        else:
            ans += "X"
    return ans


cmds = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
ans = solution(8, 2, cmds)
print(ans)