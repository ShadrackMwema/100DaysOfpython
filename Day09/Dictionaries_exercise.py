student_scores ={
    "shad":80,
    "manu":70,
    "Rolex":54,
    "Rose":76,
    "JOhn":60,
    
    
}

student_grades ={}
for key in student_scores:

    if student_scores[key] >70:
        student_grades[key] = "Grade A"
    elif student_scores[key] <= 70 and student_scores[key] >=50:
        student_grades[key] = "Grade B"
    else :
        student_grades[key] = "Grade C"

print(student_grades)