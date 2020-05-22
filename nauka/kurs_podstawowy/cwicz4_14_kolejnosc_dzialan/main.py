shoesize = 38
action = ((shoesize * 5 + 50) * 20 + 1020) - 1993
print(action)

something = (7 * 2 + 10) / 2 - 7
print(something)

a = 2 + 2 * 2
print(a)

b = 7 + 7 / 7 + 7 * 7 - 7
print(b)

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