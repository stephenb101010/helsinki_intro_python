def read_file(file_name):
    file_name = file_name.lower()
    with open(file_name) as file:
        if 'students' in file_name or 'exercises' in file_name or 'exam_points' in file_name:
            dict = {}
            for line in file:
                line = line.replace('\n', '')
                line_as_list = line.split(';')
                if line_as_list[0] == 'id':
                    continue
                dict[line_as_list[0]] = line_as_list[1:]
            return dict
        elif 'course' in file_name:
            course_info = []
            for line in file:
                line = line.replace('\n', '')
                line_as_list = line.split(':')
                course_info.append(line_as_list[1].strip())
            return course_info

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

def write_results(students, exercises, exams, course, results_file_name):
    label_name = 'name'
    exec_nbr = 'exec_nbr'
    exec_pts = 'exec_pts.'
    exm_pts = 'exm_pts.'
    tot_pts = 'tot_pts.'
    grade = 'grade'

    students_grade = []
    report = ''
    report += (f'{course[0]}, {course[1]} credits') + '\n'
    report += ('======================================') + '\n'
    report += (f'{label_name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade:10}') + '\n'
    for id, name in students.items():
        exercise_total = sum(exercises[id])
        exercise_points = int(((exercise_total/40)*100)//10)
        exam_points = sum(exams[id])
        total_points = exercise_points+exam_points
        grade = points_to_grade(total_points)
        full_name = name[0] + ' ' + name[1]
        students_grade.append([str(id), full_name, str(grade)])
        report += (f'{full_name:30}{exercise_total:<10}{exercise_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}') + '\n'

    results_txt_file_name = results_file_name + '.txt'
    results_csv_file_name = results_file_name + '.csv'
    with open(results_txt_file_name, 'w') as results_txt_file:
        results_txt_file.write(report)
    with open(results_csv_file_name, 'w') as results_csv_file:
        for record in students_grade:
            line = ';'.join(record) + '\n'
            results_csv_file.write(line)
    print(f'Results written to files {results_txt_file_name} and {results_csv_file_name}')

def main():
    if True:
        student_file = input('Student information: ')
        exercises_file = input('Exercises completed: ')
        exam_file = input('Exam points: ')
        course_file = input('Course information: ')
    else:
        student_file = 'students1.csv'
        exercises_file = 'exercises1.csv'
        exam_file = 'exam_points1.csv'
        course_file = 'course1.txt'

    results_file = 'results'

    students = read_file(student_file)
    exercises = read_file(exercises_file)
    exams = read_file(exam_file)
    course = read_file(course_file)

    convert_dict_values_list_str_to_int(exercises)
    convert_dict_values_list_str_to_int(exams)

    write_results(students, exercises, exams, course, results_file)
main()

'''
student_data = input("Student information: ")

exercise_data = input("Exercises completed: ")

exam_data = input("Exam points: ")

course_data = input("Course information: ")

 

def get_grade(points):

    a = 0

    limits = [15, 18, 21, 24, 28]

    while a < 5 and points >= limits[a]:

        a += 1

    return a

 

def as_score(number):

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

 

with open(course_data) as file:

    rows = []

    for row in file:

        rows.append(row)

 

    course_name = rows[0][5:].strip()

    credits = int(rows[1][14:])

 

with open("results.txt", "w") as file:

    header = f"{course_name}, {credits} credits\n"

    file.write(header)

    separator = "="*(len(header)-1)

    file.write(f"{separator}\n")

    file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")

    for student_id, name in students.items():

        exer = exercises[student_id]

        exer_score = as_score(exer)

        exam_pts = exams[student_id]

        tot_score = exer_score + exam_pts

        file.write(f"{name:30}{exer:<10}{exer_score:<10}{exam_pts:<10}{tot_score:<10}{get_grade(tot_score):<10}\n")

 

with open("results.csv", "w") as file:

    for student_id, name in students.items():

        exer = exercises[student_id]

        exer_score = as_score(exer)

        exam_pts = exams[student_id]

        tot_score = exer_score + exam_pts

        row = ";".join([student_id, name, str(get_grade(tot_score))])

        file.write(f"{row}\n")
'''