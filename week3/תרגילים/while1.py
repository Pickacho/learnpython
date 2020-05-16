def get_grades(number_of_grades):
    grades = []
    while len(grades) < number_of_grades:
        current_grade = int(input("Please enter a student grade: "))
        grades = grades + [current_grade]
    return grades


def get_highest_grade(grades):
    highest_grade = grades[0]
    current_grade_index = 1
    while current_grade_index < len(grades):
        if grades[current_grade_index] > highest_grade:
            highest_grade = grades[current_grade_index]
        current_grade_index = current_grade_index + 1
    return highest_grade


number_of_grades = int(input("How many students are there?: "))
grades = get_grades(number_of_grades)
highest_grade = get_highest_grade(grades)
print(f"The highest grade is {highest_grade}")
