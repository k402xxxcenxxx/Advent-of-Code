def solver(filepath: str) -> int:

    letter_matrix = {
        "o": {
            "one": 1,
        },
        "t": {
            "two": 2,
            "three": 3
        },
        "f": {
            "four": 4,
            "five": 5
        },
        "s": {
            "six": 6,
            "seven": 7
        },
        "e": {
            "eight": 8,
        },
        "n": {
            "nine": 9,
        }
    }

    res = 0
    with open(filepath, "r") as fd:
        line = fd.readline()

        while line is not None and line != '':
            d1 = -1
            for idx, c in enumerate(line):
                if ord('0') <= ord(c) <= ord('9'):
                    if d1 == -1:
                        d1 = int(c)
                    d2 = int(c)
                # check if the leading char match the possible text
                elif letter_matrix.get(c) is not None:
                    for k in letter_matrix[c].keys():
                        if line[idx:idx+len(k)] == k:
                            if d1 == -1:
                                d1 = letter_matrix[c][k]
                            d2 = letter_matrix[c][k]
                            break

            res += d1 * 10 + d2

            line = fd.readline()

    return res
