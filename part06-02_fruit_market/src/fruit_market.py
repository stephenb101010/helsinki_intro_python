def read_fruits():
    fruits_dict = {}
    with open("fruits.csv") as fruits:
        for line in fruits:
            line = line.strip("\n")
            parts = line.split(";")
            fruits_dict[parts[0]] = float(parts[1])
    return fruits_dict