def directory_path(input_path):
    if not input_path:
        raise ValueError("Empty path as input")
    
    result = []
    if input_path[0] == "/":
        result.append("/")
    split_path = [x for x in input_path.split("/") if x not in ["", "."]]
    for _dir in split_path:
        if _dir == "..":
            if not result or result[-1] == "..":
                result.append(_dir)
            else:
                if result[-1] == "/":
                    raise ValueError("Incorrect path")
                result.pop()
        else:
            result.append(_dir)
    result = "/".join(result)
    return result[1:]

if __name__ == "__main__":
    path = "/usr/lib/../lib/bin"
    print "Short path for ", path, " is ",
    print directory_path(path)

    path = "/usr/lib/../../bin"
    print "Short path for ", path, " is ",
    print directory_path(path)

    # Error
    path = "/../usr/lib/../../bin"
    print "Short path for ", path, " is ",
    print directory_path(path)
    
