class StringProcessor:
    def __init__(self, String):
        self.string = String

    def processString(self):
        myString = ""
        for char in self.string:
            if char.isalnum():
                myString += char.lower()
        return myString