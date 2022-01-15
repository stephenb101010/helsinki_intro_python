from datetime import datetime, timedelta

if True:
    filename = input("Filename: ")
    start_date = input("Starting date: ")
    num_days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    start_day = datetime.strptime(start_date, "%d.%m.%Y")
    last_day = start_day + timedelta(days=num_days)

    days = []
    times = []
    while start_day < last_day:
        day = start_day.strftime("%d.%m.%Y")
        days.append(day)
        screen_time = input(f"Screen time {day}: ")
        times.append(tuple(screen_time.split(" ")))
        start_day = start_day + timedelta(days=1)
else:
    # Used during development for quick testing.
    filename = "late_june.txt"
    start_date = "24.6.2020"
    num_days = 5
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    start_day = datetime.strptime(start_date, "%d.%m.%Y")
    last_day = start_day + timedelta(days=num_days)

    times = [("60","120","0"), ("0","0","0"), ("180","0","0"), ("25","240","15"), ("45","90","5")]
    days = ["24.06.2020", "25.06.2020", "26.06.2020", "27.06.2020", "28.06.2020"]

print(f"Data stored in file {filename}")
with open(filename, "w") as file:
    file.write(f"Time period: {days[0]}-{days[num_days-1]}\n")
    total_time = 0
    for time in times:
        total_time += int(time[0]) + int(time[1]) + int(time[2])
    file.write(f"Total minutes: {total_time}\n")
    file.write(f"Average minutes: {total_time/len(times)}\n")
    for index, day in enumerate(days):
        file.write(f"{day}: {times[index][0]}/{times[index][1]}/{times[index][2]}\n")

"""
from datetime import datetime, timedelta

week = timedelta(days=7)

def format(aika):
    return aika.strftime("%d.%m.%Y")

file = input("Filename: ")
start = input("Starting date: ").split(".")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))
for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(" ")
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )

with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
print(f"Data stored in file {file}")
"""