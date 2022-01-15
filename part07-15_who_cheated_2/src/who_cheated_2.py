import csv
import json
from datetime import datetime, timedelta

def get_students_exam_data() -> dict:
    students = {}
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            student = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")
            students[student] = {
                "start_time" : start_time,
                #"start_time" : line[1],
                "stats" : {
                    "tasks" : [],
                    "points" : [],
                    "submission_times" : []
                }
            }

    with open("submissions.csv") as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            student = line[0]
            task = int(line[1])
            point = int(line[2])
            sub_time = datetime.strptime(line[3], "%H:%M")
            students[student]["stats"]["tasks"].append(task)
            students[student]["stats"]["points"].append(point)
            students[student]["stats"]["submission_times"].append(sub_time)
            #students[student]["stats"]["submission_times"].append(line[3])

    return students

def final_points():
    final_points = {}
    data = get_students_exam_data()
    for student, info in data.items():
        total_points = 0
        start_time = info["start_time"]
        tasks = info["stats"]["tasks"]
        for task in range(1, 9):
            indices = [i for i, v in enumerate(tasks) if v == task]
            max_point = 0
            for index in indices:
                point = info["stats"]["points"][index]
                sub_time = info["stats"]["submission_times"][index]
                if sub_time <= (start_time + timedelta(hours=3)):
                    if point > max_point:
                        max_point = point
            total_points += max_point
        final_points[student] = total_points
    return final_points

"""
import csv
from datetime import datetime, timedelta

def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
        # Then read submissions
        # From each student time and points is saved to a dictionary
        # Time and points is saved as tuple.
        points = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            tno = int(row[1])
            p = int(row[2])
            time = datetime.strptime(row[3], "%H:%M")
            # If cheating has happened, submission is not handled
            if time - start_times[name] > timedelta(hours=3):
                continue
            # If student is not handled yet, add student directly to the dictionary
            if name not in points:
                default_time = datetime(1900, 1, 1)
                points[name] = {}
                for i in range(1, 8+1):
                    points[name][i] = 0
                points[name][tno] = p
            # If student already exists, more points than earlier is required
            elif p > points[name][tno]:
                points[name][tno] = p

        final_points = {}
        # Iterate through students one by one
        for student in points:
            p = 0
            for exercise in points[student]:
                p += points[student][exercise]
            final_points[student] = p
        return final_points
"""