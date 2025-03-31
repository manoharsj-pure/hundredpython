student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for score in student_scores:
    if student_scores[score] < 100 and student_scores[score] > 91:
        student_scores[score] = "Outstanding"
    elif student_scores[score] < 90 and student_scores[score] > 81:
        student_scores[score] = "Exceeds Expectations"
    elif student_scores[score] < 80 and student_scores[score] > 71:
        student_scores[score] = "Acceptable"
    elif student_scores[score] <= 70:
        student_scores[score] = "Fail"

student_grades = student_scores