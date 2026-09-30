def rearrange(string):
    seen = set()
    result = []
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
        else:
            for ch in string:
                if ch not in seen:
                    seen.add(ch)
                    result.append(ch)
    return ''.join(result)