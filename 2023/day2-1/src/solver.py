def solver(filepath: str, r: int, g: int, b: int) -> int:

    res = 0
    with open(filepath, "r") as fd:
        line = fd.readline()

        while line is not None and line != '':

            sub_lines = line.split(":")
            id = int(sub_lines[0][sub_lines[0].find(" "):])

            is_valid = True

            games_lines = sub_lines[1].split(";")
            for game in games_lines:

                color_lines = game.split(",")

                for color in color_lines:
                    c = color.strip()
                    sep_idx = c.find(" ")
                    match c[sep_idx+1:]:
                        case "red"  : possible_num = r
                        case "green": possible_num = g
                        case "blue" : possible_num = b
                        case _ : raise Exception(f"Unknown color char: {c[sep_idx+1:]}")

                    if int(c[:sep_idx]) > possible_num:
                        is_valid = False

            if is_valid:
                res += id

            line = fd.readline()

    return res
