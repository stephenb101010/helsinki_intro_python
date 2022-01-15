def list_total(nums):
    total = 0
    for n in nums:
        total += n
    return total

def list_max(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def matrix_sum():
    with open("matrix.txt") as file:
        file_total = 0
        for line in file:
            line = line.strip("\n")
            nums_str = line.split(",")
            nums = []
            for n in nums_str:
                nums.append(int(n))
            file_total += list_total(nums)
        return file_total

def matrix_max():
    with open("matrix.txt") as file:
        file_max = -100000000
        for line in file:
            line = line.strip("\n")
            nums_str = line.split(",")
            nums = []
            for n in nums_str:
                nums.append(int(n))
            if list_max(nums) > file_max:
                file_max = list_max(nums)
        return file_max

def row_sums():
    with open("matrix.txt") as file:
        file_row_sums = []
        for line in file:
            line = line.strip("\n")
            nums_str = line.split(",")
            nums = []
            for n in nums_str:
                nums.append(int(n))
            file_row_sums.append(list_total(nums))
        return file_row_sums

"""
def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
    return m

# Merges rows in an array into a single list
def combine(matriisi: list):
    mlist = []
    for row in matriisi:
        mlist += row
    return mlist

def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)

def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)

def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums
"""