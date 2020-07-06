with open("csv2line.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)
