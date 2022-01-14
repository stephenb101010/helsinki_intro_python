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

def print_stats(students, exercises, exams):
    label_name = "name"
    exec_nbr = "exec_nbr"
    exec_pts = "exec_pts."
    exm_pts = "exm_pts."
    tot_pts = "tot_pts."
    grade = "grade"

    print(f"{label_name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade:10}")
    for id, name in students.items():
        exercise_total = sum(exercises[id])
        exercise_points = int(((exercise_total/40)*100)//10)
        exam_points = sum(exams[id])
        total_points = exercise_points+exam_points
        grade = points_to_grade(total_points)
        full_name = name[0] + " " + name[1]
        print(f"{full_name:30}{exercise_total:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}")

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

    print_stats(students, exercises, exams)

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

print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for eid, name in students.items():
    exec_nbr = exercises[eid]
    exec_score = to_points(exec_nbr)
    exam_points = exams[eid]
    total_points = exec_score + exam_points
    print(f"{name:30}{exec_nbr:<10}{exec_score:<10}{exam_points:<10}{total_points:<10}{grade(total_points):<10}")
'''