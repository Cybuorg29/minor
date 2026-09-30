def area(shape):
    if shape == "rectangle":
        length = float(input("Please enter the length: "))
        width = float(input("Please enter the width: "))
        return length * width

    elif shape == "triangle":
        base = float(input("Please enter the base: "))
        height = float(input("Please enter the height: "))
        return 0.5 * base * height

    elif shape == "circle":
        r = float(input("Please enter the radius: "))
        return 3.14 * r * r