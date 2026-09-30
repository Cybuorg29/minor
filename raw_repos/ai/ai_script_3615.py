def remove_duplicates(original_list, key):
    seen = set()
    new_list = [item for item in original_list if key not in seen and (seen.add(item[key]) if item[key] is not None else True)]
    return new_list