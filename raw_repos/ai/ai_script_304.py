"""
Java class to store the number of letters, numbers and special characters in a given string
"""

public class StringInfo {
    // Instance Variables 
    int letterCount;
    int numberCount;
    int specialCharCount;

    // Constructor to initialize all the instance variables
    public StringInfo() {
        this.letterCount = 0;
        this.numberCount = 0;
        this.specialCharCount = 0;
    }

    // A method to find the count of letters, numbers and special characters in a given string
    public void findCounts(String str) {
        // Loop through each character in the string
        for (char c : str.toCharArray()) {
            if (Character.isLetter(c)) {
                letterCount++;
            } else if (Character.isDigit(c)) {
                numberCount++;
            } else {
                specialCharCount++;
            }
        }
    }

    // Accessor methods to get the count of each type of character
    public int getLetterCount() {
        return letterCount;
    }

    public int getNumberCount() {
        return numberCount;
    }

    public int getSpecialCharCount() {
        return specialCharCount;
    }
}