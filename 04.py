students = ["Еремян", "Степин", "Чепля", "Леськов"]
course = ["Высшая математика", "Теория систем", "Бух.учёт", "Алгоритмизация"]
dates = ["03.07.26","03.06.26","03.05.26","03.04.26"]
grades = [1,2,3,4,5]
zero = [0, 1, 2, 3]

for c in zero:
    if course[c] == "Бух.учёт":
        for d in zero:
            if dates[d] == "03.05.26":
                for s in zero:
                    if students[s] == students[1]:
                        for g in grades:
                            print(students[s], g, course[c], dates[d])
