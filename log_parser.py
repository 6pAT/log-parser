import time
import os
import error_level
import warn_level
import info_level
import duplicate
import re

__author__ = "Artem Kharchishin"

INPUT_FILE_NAME = "input"
OUTPUT_FILE_NAME = "output"
work_time = time.time()


def exit_script(code, start_work_time):
    print "Working time {} secs".format(int(time.time() - start_work_time))
    exit(code)


def load_input():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), INPUT_FILE_NAME)
    if not os.path.exists(file_path):
        print "Not found input file."
        with open(file_path, 'w') as f:
            f.write("input")
        print "Write default input file in " + file_path
        exit_script(0, work_time)
    else:
        print "Input file found " + file_path
        input_file = open(file_path, "r")
        return input_file.readlines()


def write_output(output):
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), OUTPUT_FILE_NAME)
    output_file = open(file_path, "w")
    output_file.write(output)
    output_file.close()


def main():
    input_file = load_input()

    other_log = []
    time_pattern = re.compile('\([0-9][0-9]:[0-9][0-9]:[0-9][0-9]\)')
    parsers = [
        error_level,
        warn_level,
        info_level,
        duplicate
    ]
    for line in input_file:
        if time_pattern.match(line):
            line = line[11:]

        parsed = False
        for parser in parsers:
            parsed = parser.parse(line) or parsed

        if not parsed:
            other_log.append(line)

    output = ""
    for parser in parsers:
        output += parser.get_output()
    output += "=" * 80
    output += "\n\tOTHER\n"
    output += "=" * 80 + "\n"
    output += "\t" + "\t".join(other_log)

    write_output(output)

    print "Working time {} secs".format(int(time.time() - work_time))


if __name__ == "__main__":
    main()
