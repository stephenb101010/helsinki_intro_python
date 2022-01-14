def read_file(file_name):
    with open(file_name) as file:
        dict = {}
        for line in file:
            line = line.strip("\n")
            line_as_list = line.split(";")
            if line_as_list[0] == "id":
                continue
            dict[line_as_list[0]] = line_as_list[1:]
        return dict

def convert_dict_values_list_str_to_int(dict):
    for key, value in dict.items():
        for list_index, list_value in enumerate(value):
            value[list_index] = int(list_value)

def points_to_grade(points):
    grade = -1
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5

def main():
    if True:
        student_file = input("Student information: ")
        exercises_file = input("Exercises completed: ")
        exam_file = input("Exam points: ")
    else:
        student_file = "students1.csv"
        exercises_file = "exercises1.csv"
        exam_file = "exam_points1.csv"

    students = read_file(student_file)
    exercises = read_file(exercises_file)
    exams = read_file(exam_file)

    convert_dict_values_list_str_to_int(exercises)
    convert_dict_values_list_str_to_int(exams)

    for id, name in students.items():
        exercise_points = int(((sum(exercises[id])/40)*100)//10)
        exam_points = sum(exams[id])
        grade = points_to_grade(exercise_points+exam_points)
        print(f"{name[0]} {name[1]} {grade}")

main()

'''
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    return a

def to_points(number):
    return number // 4

students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum

exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum
 
for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    print(f"{name} {grade(total)}")
'''