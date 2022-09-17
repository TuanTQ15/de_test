def read_csv(path):
    data = []
    try:
        with open(path) as infile:
            try:
                raw_data = infile.read().splitlines()
                for line in raw_data:
                    if len(line.strip()) == 0: 
                        continue
                    if ',' not in line:
                        continue
                    line_result = []
                    found_quote = False
                    element = ""
                    #"abc, def", def123
                    #True
                    #elemet=abc,
                    for c in line:
                        if c == '"':
                            found_quote = not found_quote
                            continue
                        if c == ",":
                            if found_quote:
                                element += c
                            else:
                                line_result.append(element)
                                element = ""
                        else:
                            element += c

                    line_result.append(element)
                    data.append(line_result)
            except (IOError, OSError):
                return "Error while reading file"
    except (FileNotFoundError, PermissionError, OSError):
        return "Error opening file"
    return data