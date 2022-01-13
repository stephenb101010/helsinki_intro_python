def count_matching_elements(my_matrix: list, element: int):
    num_of_matches = 0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])): 
            if my_matrix[i][j] == element:
                num_of_matches += 1
    return num_of_matches