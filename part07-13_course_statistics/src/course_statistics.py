import urllib.request
import json
from math import floor

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    active = []
    for course in courses:
        if course["enabled"] == True:
            tup = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            active.append(tup)
    return active

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course = json.loads(data)
    # json_formatted_str = json.dumps(course, indent=2)
    # print(json_formatted_str)
    course_info = {}
    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    for week, data in course.items():
        weeks += 1
        if data["students"] > students:
            students = data["students"]
        hours += data["hour_total"]
        exercises += data["exercise_total"]
    hours_average = floor(hours/students)
    exercises_average = floor(exercises/students)

    course_info["weeks"] = weeks
    course_info["students"] = students
    course_info["hours"] = hours
    course_info["hours_average"] = hours_average
    course_info["exercises"] = exercises
    course_info["exercises_average"] = exercises_average

    return course_info

"""
import urllib.request
import json

def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats/api/courses")
    course_data = json.loads(request.read())
    courses = []
    for course in course_data:
        if not course["enabled"]:
            continue
        exercises = 0
        for exercise in course["exercises"]:
            if exercise:
                exercises += exercise
        courses.append((course["fullName"], course["name"], course["year"], exercises))
    return courses

def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats/api/courses/{course_name}/stats")
    course_weeks = json.loads(request.read())
    students = 1
    exercises = 0
    hours = 0 
    for no, week in course_weeks.items():
        if week["students"] > students:
            students = week["students"]
        hours += week["hour_total"]
        exercises += week["exercise_total"]
    return {
        "weeks": len(course_weeks),
        "students": students,
        "hours": hours,
        "hours_average": hours//students,
        "exercises": exercises,
        "exercises_average": exercises//students,
    }
"""