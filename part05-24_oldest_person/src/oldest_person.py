def oldest_person(people: list):
    oldest_age = people[0][1]
    oldest_name = people[0][0]
    for person in people:
        if oldest_age > person[1]:
            oldest_age = person[1]
            oldest_name = person[0]
    return oldest_name

'''
    oldest = people[0]
    for person in people:
        # comparing the year of birth of the oldest known person and the person in turn
        if person[1] < oldest[1]:
            oldest = person

    return oldest[0]
'''