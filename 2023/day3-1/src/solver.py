def solver(filepath: str) -> int:

    res = 0
    # engine_schematic
    data = []
    with open(filepath, "r") as fd:
        for line in fd.readlines():
            data.append(line)

    rows = len(data)
    cols = len(data[0])

    def sub_solver(y: int, x: int) -> tuple[int, int]:
        is_valid = False
        res = 0
        x_offset = 0

        while x + x_offset < cols:
            cur_x = x + x_offset
            x_offset += 1

            if ord('0') <= ord(data[y][cur_x]) <= ord('9'):
                # Check surrounding
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if 0 <= cur_x + dx < cols \
                            and 0 <= y + dy < rows \
                            and data[y + dy][cur_x + dx] != '.' \
                            and data[y + dy][cur_x + dx] != '\n' \
                            and not ((ord('0') <= ord(data[y + dy][cur_x + dx]) <= ord('9'))):
                            is_valid = True

                # calculate number
                res = 10 * res + int(data[y][cur_x])
            else:
                break

        if not is_valid:
            res = 0

        return res, x_offset

    y = 0
    while y < rows:
        x = 0
        while x < cols:
            sub_res, x_offset = sub_solver(y, x)
            res += sub_res
            x += x_offset
        y += 1

    return res
