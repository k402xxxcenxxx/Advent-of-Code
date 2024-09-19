def solver(filepath: str) -> int:
    res = 0
    with open(filepath, "r") as fd:
        line = fd.readline()

        while line is not None and line != '':
            d1 = -1
            for c in line:
                if ord('0') <= ord(c) <= ord('9'):
                    if d1 == -1:
                        d1 = int(c)
                    d2 = int(c)

            res += d1 * 10 + d2

            line = fd.readline()

    return res
