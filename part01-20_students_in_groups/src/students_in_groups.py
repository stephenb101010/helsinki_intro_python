# Write your solution here
number_students = int(input("How many students on the course? "))
desired_groupsize = int(input("Desired group size? "))
number_groups = number_students // desired_groupsize
groups_even = number_students % desired_groupsize
if groups_even != 0:
    print(f"Number of groups formed: {number_groups + 1}")
else:
    print(f"Number of groups formed: {number_groups}")