def write_to_file(d):
    #get the row with maximum number of columns
    maxrowlen = 0
    maxrowkey = ""
    for timesid in d.keys():
        if len(timesid.keys()) > maxrowlen:
            maxrowlen = len(timesid.keys())
            maxrowkey = timesid
    maxrowcols = sorted(d[maxrowkey].keys())

    # prepare the writing
    cell_format = "%10r"    # or whatever suits your data

    # create the output string
    lines = []
    for timesid in d.keys(): # go through all times
        line = ""
        for col in maxrowcols:  # go through the standard columns
            colstr = ""
            if col in d[timesid].keys():   # create an entry for each standard column
                colstr += cell_format % d[timesid][col]  # either from actual data
            else:
                colstr += cell_format % ""                      # or blanks
            line += colstr
        lines.append(line)

    text = "\n".join(lines)

    with open(arquivo, 'w') as f:
        f.writelines(text)