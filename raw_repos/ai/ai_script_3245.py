def remove_string(remove, string):
    return string.replace(remove, "")

remove_string("cat", "The crazy cat jumped to the roof")
# Output: "The crazy  jumped to the roof"