def strip_tags(s):
    tag = False
    out = ""
    for c in s:
        if c == "<":
            tag = True
        elif c == ">":
            tag = False
        elif not tag:
            out += c
    return out