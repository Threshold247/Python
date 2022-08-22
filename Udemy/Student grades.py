student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    if student_scores[names] >= 91:
        student_grades[names] = "Outstanding"
    elif student_scores[names] >= 81:
        student_grades[names] = "Exceeds Expectations"
    elif student_scores[names] >= 71:
        student_grades[names] = "Acceptable"
    else:
        student_scores[names] = "Fail"
print(student_grades)
