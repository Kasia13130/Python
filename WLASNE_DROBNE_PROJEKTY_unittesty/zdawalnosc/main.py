presence = 0.85
note = 3.5
semesterWork = False

passedTheSemester = presence and note >= 3.0 or semesterWork
print("The student: ", passedTheSemester)

presence = 0.85
note = 3.0
semesterWork = True

passedTheSemester = presence and note >= 3.0 and semesterWork
print("The student: ", passedTheSemester)

presence = 0.40
note = 2.5
semesterWork = True

passedTheSemester = presence and note >= 3.0 and semesterWork
print("The student: ", passedTheSemester)