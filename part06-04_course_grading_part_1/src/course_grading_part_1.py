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

def list_str_to_int(list):
    for index, value in enumerate(list):
        list[index] = int(value)

def main():
    if True:
        student_file = input("Student information: ")
        exercises_file = input("Exercises completed: ")
    else:
        student_file = "students1.csv"
        exercises_file = "exercises1.csv"

    students = read_file(student_file)
    exercises = read_file(exercises_file)

    for id, exercises_list in exercises.items():
        list_str_to_int(exercises_list)

    for id, name in students.items():
        exercises_total = sum(exercises[id])
        print(f"{name[0]} {name[1]} {exercises_total}")

main()

'''
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

for student_id, name in students.items():
    print(f"{name} {exercises[student_id]}")
'''