"""
Calculate the average of a given list of grades
"""

def average(grades):
    sum = 0
    for grade in grades:
        sum += grade
    
    return sum / len(grades)

if __name__ == '__main__':
    grades = [90, 95, 80, 75]
    print(average(grades))