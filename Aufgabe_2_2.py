__author__ = "6611082: Cedric Reuter"

valid_grades = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0]


def split_input(input_text):
    words = input_text.split()
    return words


def get_grade():
    grade = 0.0
    sex = "w"
    height = 100

    a = input('--> ')
    words = split_input(a)
    if(not len(words) == 3):
        print("ERROR")
        return
    grade = words[0]
    sex = words[1]
    height = words[2]

    try:
       grade = float(grade)
    except ValueError:
        print("ERROR")
        return
    if(not grade in valid_grades):
        print("ERROR")
        return
    if(not sex.isalpha()):
        print("ERROR")
        return
    if (not height.isdigit()):
        print("ERROR")
        return
    height = int(height)
    if (not height >= 100) or (not height <= 300):
        print("ERROR")
        return
    if(sex == "w"):
        grade -= 0.4
    if(height > 180):
        bonus = (height - 180) * 0.05
        grade += bonus
    grade = round_grade(grade)
    print(grade)


def round_grade(grade):
    min = 10
    if(grade > 4.0):
        return 5.0
    for x in range(11):
        if (abs(grade-valid_grades[x]) < min):
            min = abs(grade-valid_grades[x])
            minpos = x
    min = valid_grades[minpos]
    return min

get_grade()
