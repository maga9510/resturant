# def main(x):
#     open = {
#         "{": 1,
#         "(": 2,
#         "[":3,
#     }
#     close = {
#         "}":1,
#         ")":2,
#         "]":3,
#     }
#     q = len(x)
#     if q % 2 != 0:
#         return False
#     if q == 2 and open[x[0]] == close[x[1]]:
#         return True
#     elif open[x[0]] == close[x[-1]]:
#         x = x[1:-2]
#         return main(x)
#     elif open[x[0]] == close[x[1]]:
#         x = x[2:]
#         return main(x)
#     else:
#         op = []
#         op.appe
#         False
a = "[]()[()()][{}]()"


def main(x):
        if len(x) %2 == 0:
            open = {
                "{": 1,
                "(": 2,
                "[":3,
            }
            close = {
                "}":1,
                ")":2,
                "]":3,
            }
            while True:
                q = len(x)
                y = x
                for i in range(q-1):
                    try:
                        if len(y) <= i:
                            break
                        if open[y[i]] == close[y[i+1]]:
                            y = y[0:i] + y[i+2:]
                        if open[y[0]] == close[y[-1]]:
                            y = y[1:-1]
                    except KeyError:
                        continue
                    except IndexError:
                        continue
                w = len(y)
                if w == 0:
                    return True
                if q > w:
                    x= y
                if q == w:
                    return False
        else:
            return False
print(main(a))

