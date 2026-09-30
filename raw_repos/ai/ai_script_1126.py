def group_students_by_major(student_list):
    # create a dictionary with two empty lists 
    student_groups = {"Computer Science": [], "Business Administration": []}
    # iterate through the student list
    for student in student_list:
        # for each student in the list, add their name to the respective list
        student_groups[student["major"]].append(student["name"])
    # return the dictionary of groups
    return student_groups