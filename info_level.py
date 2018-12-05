log = []


def has_in(line):
    return "Info:" in line


def parse(line):
    if not has_in(line):
        return False

    log.append(line)

    return True


def get_output():
    output = "=" * 80
    output += "\n\tINFO\n"
    output += "=" * 80 + "\n"
    if len(log) > 0:
        output += "\t" + "\t".join(log)
        output += "\n"
    return output
