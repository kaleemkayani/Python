students = ["Kaleem", "Alyan", "Baseer", "Faryad"]
for student in students:
    if(student == "Faryad"):
        break
    print(student)

    for student in students:
        if (student == "Kaleem"):
            continue
        print(student)
