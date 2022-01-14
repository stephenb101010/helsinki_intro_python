def read_file(file_name: str) -> list:
    with open(file_name) as file:
        content = []
        for line in file:
            line = line.replace('\n','')
            line = line.split(';')
            content.append(line)
        return content

def evaluate_data(content: list, correct_file_name: str, incorrect_file_name: str):
    open(correct_file_name, 'w').close()
    open(incorrect_file_name, 'w').close()
    correct_file = open(correct_file_name, 'w')
    incorrect_file = open(incorrect_file_name, 'w')
    for solution in content:
        sol = ';'.join(solution)
        sol += '\n'
        if eval(solution[1]) == int(solution[2]):
            correct_file.write(sol)
        else:
            incorrect_file.write(sol)
    correct_file.close()
    incorrect_file.close()

def filter_solutions():
    content = read_file('solutions.csv')
    evaluate_data(content, 'correct.csv', 'incorrect.csv')

'''
def filter_solutions():

    # Open all lines

    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:

        for row in source:

            # Split into pieces

            pieces = row.split(";")

 

            calculation = pieces[1]

            result = pieces[2]

 

            # Addition or subtraction?

            if "+" in calculation:

                operands = calculation.split("+")

                # correct is True or False based on whether the calculation was correct or not

                correct = int(operands[0]) + int(operands[1]) == int(result)

            else:

                operands = calculation.split("-")

                # correct is True or False based on whether the calculation was correct or not

                correct = int(operands[0]) - int(operands[1]) == int(result)

 

            # Write to file

            if correct:

                correct_file.write(row)

            else:

                incorrect_file.write(row)s
'''