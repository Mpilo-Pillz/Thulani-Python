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
for student_score in student_scores:
    if student_scores[student_score] >= 91 and student_scores[student_score] <= 100:
        student_grades[student_score] = "Outstanding"
    elif student_scores[student_score] >= 81 and student_scores[student_score] <= 90:
        student_grades[student_score] = "Exceeds Expectations"
    elif student_scores[student_score] >= 71 and student_scores[student_score] <= 80:
        student_grades[student_score] = "Acceptable"
    else:
        student_grades[student_score] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)