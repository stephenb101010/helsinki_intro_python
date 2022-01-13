def convert_exercise_completed_to_points(exercise : int):
    return exercise // 10

def calculate_grade(exam : int, exercise : int):
    total = exam + exercise
    if exam < 10 or total <= 14:
        return 0
    elif total <= 17:
        return 1
    elif total <= 20:
        return 2    
    elif total <= 23:
        return 3
    elif total <= 27:
        return 4
    elif total <= 30:
        return 5
    else:
        return None

def points_avg(exam_points : list, exercise_points: list):
    sum = 0
    for i in range(len(exam_points)):
        sum += exam_points[i] + exercise_points[i]
    return sum/len(exam_points)

def pass_percent(exam_points : list, exercise_points : list):
    pass_count = 0
    for i in range(len(exam_points)):
        grade = calculate_grade(exam_points[i], exercise_points[i])
        if grade > 0:
            pass_count += 1
    return (pass_count/len(exam_points))*100

def grade_distribution(exam_points : list, exercise_points : list):
    grades = []
    for i in range(len(exam_points)):
        grade = calculate_grade(exam_points[i], exercise_points[i])
        grades.append(grade)

    print("Grade distribution:")
    grade = 5
    while grade >= 0:
        stars = "*"*grades.count(grade)
        print(f"  {grade}: {stars}")
        grade -= 1

def generate_stats(exam_points : list, exercise_points : list):
    print("Statistics:")
    print(f"Points average: {points_avg(exam_points, exercise_points):.1f}")
    print(f"Pass percentage: {pass_percent(exam_points, exercise_points):.1f}")
    grade_distribution(exam_points, exercise_points)

def main():
    exam_points = []
    exercise_points = []

    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            break
        exam_points.append(int(points.split()[0]))
        exercise_completed = int(points.split()[1])
        exercise_points.append(convert_exercise_completed_to_points(exercise_completed))

    generate_stats(exam_points, exercise_points)

main()

'''
def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]

def exercise_points(amount):
    return amount // 10

def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i

def mean(points):
    return sum(points) / len(points)

def main():
    points = []
    grades = [0] * 6
    
    while True:

        inpt = input("Exam points and exercises completed: ")

        if len(inpt) == 0:
            break

        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
        points.append(total_points)
        grd = grade(total_points)

        if exam_and_exercises[0] < 10:
            grd = 0

        grades[grd] += 1

    pass_pros = 100 * (len(points) - grades[0]) / len(points)
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")

main()
'''