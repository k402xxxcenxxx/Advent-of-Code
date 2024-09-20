def solver(filepath: str) -> int:

    res = 0
    with open(filepath, "r") as fd:
        line = fd.readline()

        while line is not None and line != '':

            r = 0
            g = 0
            b = 0

            sub_lines = line.split(":")
            games_lines = sub_lines[1].split(";")
            for game in games_lines:

                color_lines = game.split(",")

                for color in color_lines:
                    c = color.strip()
                    sep_idx = c.find(" ")
                    match c[sep_idx+1:]:
                        case "red": r = max(r, int(c[:sep_idx]))
                        case "green": g = max(g, int(c[:sep_idx]))
                        case "blue": b = max(b, int(c[:sep_idx]))
                        case _: raise Exception(f"Unknown color char: {c[sep_idx+1:]}")

            res += r * g * b

            line = fd.readline()

    return res
