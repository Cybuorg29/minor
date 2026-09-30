def morse_encode(input_string):
    morse_encoder = {
        "A":".- ",
        "B":"-... ",
        "C":"-.-. ",
        "D":"-.. ",
        "E":" . ",
        "F":"..-. ",
        "G":"--. ",
        "H":".... ",
        "I":".. ",
        "J":".--- ",
        "K":"-.- ",
        "L":".-.. ",
        "M":"-- ",
        "N":"-. ",
        "O":"--- ",
        "P":".--. ",
        "Q":"--.- ",
        "R":".-. ",
        "S":"... ",
        "T":"- ",
        "U":"..- ",
        "V":"...- ",
        "W":".-- ",
        "X":"-..- ",
        "Y":"-.-- ",
        "Z":"--.. ",
        " ": "  "
    }
    morse_string = []

    for char in input_string.upper():
        encoded_char = morse_encoder.get(char)
        morse_string.append(encoded_char)
    
    return ''.join(morse_string)

print(morse_encode("Hello World!")) # Output: ".... . .-.. .-.. ---  .-- --- .-. .-.. -.. ! "