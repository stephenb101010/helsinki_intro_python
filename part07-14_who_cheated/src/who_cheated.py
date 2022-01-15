import csv
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

def cheaters():
    data = get_students_exam_data()
    cheaters = []
    for student, info in data.items():
        start_time = info["start_time"]
        submission_times = info["stats"]["submission_times"]
        for time in submission_times:
            if time > (start_time + timedelta(hours=3)):
                cheaters.append(student)
                break
    return cheaters

# d = {
#     "jarmo" : {
#         "start_time" : "09:00",
#         "stats" : {
#             "exercises" : ["1", "2"],
#             "points" : ["8", "10"],
#             "submission_times" : ["16:05", "19:15"]
#         }
#     }
# }import csv
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

def cheaters():
    data = get_students_exam_data()
    cheaters = []
    for student, info in data.items():
        start_time = info["start_time"]
        submission_times = info["stats"]["submission_times"]
        for time in submission_times:
            if time > (start_time + timedelta(hours=3)):
                cheaters.append(student)
                break
    return cheaters

# d = {
#     "jarmo" : {
#         "start_time" : "09:00",
#         "stats" : {
#             "exercises" : ["1", "2"],
#             "points" : ["8", "10"],
#             "submission_times" : ["16:05", "19:15"]
#         }
#     }
# }

"""
import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time

        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time

        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
        return cheaters
"""