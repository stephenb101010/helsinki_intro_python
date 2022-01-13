def add_student(students, name):
    students[name] = []

def print_student(students, name):
    if name not in students:
        print(name + ": no such person in the database")
        return
    if len(students[name]) == 0:
        print(name + ":")
        print(" no completed courses")
    else:
        print(name + ":")
        print(f" {len(students[name])} completed courses:")
        sum_grades = 0
        for course in students[name]:
            print(f"  {course[0]} {course[1]}")
            sum_grades += course[1]
        print(f" average grade {(sum_grades/len(students[name])):.1f}")

'''
    if not name in students:
        print(f"{name}: no such person in the database")
        return

    students_completed_courses = students[name]

    print(f"{name}:")

    if len(students_completed_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(students_completed_courses):} completed courses:")
        sum = 0
        for course, grade in students_completed_courses.items():
            course_grade = grade[1]
            print(f"  {course} {course_grade}")
            sum += course_grade
        print(f" average grade {sum/len(students_completed_courses):.1f}")
'''

def avg_grade(students, name):
    if name in students and len(students[name]) > 0:
        sum_grades = 0
        for course in students[name]:
            sum_grades += course[1]
        return (sum_grades/len(students[name]))


def add_course(students, name, course_and_grade):
    new_course, new_grade = course_and_grade
    if new_grade != 0:
        courses = students[name]
        for index, course in enumerate(courses):
            if new_course == course[0]:
                if new_grade > course[1]:
                    courses.pop(index)
                    courses.insert(index, course_and_grade)
                    students[name] = courses
                return
        courses.append(course_and_grade)
        students[name] = courses

'''
    students_completed_courses = students[name]
    course_name = completion[0]
    course_grade = completion[1]

    # failed course is not recorded in the database
    if course_grade==0:
        return

    # if previous grade is higher, new grade is not recorded in the database
    if course_name in students_completed_courses:
        if students_completed_courses[course_name][1] > course_grade:
            return

    students_completed_courses[course_name] = completion
'''

def summary(students):
    if len(students) > 0:
        print(f"students {len(students)}")
        max_courses_student = None
        max_courses = 0
        max_avg_grade_student = None
        max_avg_grade = 0.0
        for student, courses in students.items():
            if len(courses) > max_courses:
                max_courses = len(courses)
                max_courses_student = student

            student_avg_grade = avg_grade(students, student)
            if student_avg_grade > max_avg_grade:
                max_avg_grade_student = student
                max_avg_grade = student_avg_grade
        print(f"most courses completed {max_courses} {max_courses_student}")
        print(f"best average grade {max_avg_grade:.1f} {max_avg_grade_student}")

'''
    print(f"students {len(students)}")
    most_courses_count = 0
    best_avg_grade = 0
    for name, completions in students.items():
        if len(completions) > most_courses_count:
            most_courses = name
            most_courses_count = len(students[most_courses])

        sum = 0
        for course, grade in completions.items():
            sum += grade[1]

        if len(completions)==0:
            avg = 0
        else:
            avg = sum/len(completions)

        if avg>best_avg_grade:
            best_avg_grade = avg
            best = name
    
    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best}")
'''