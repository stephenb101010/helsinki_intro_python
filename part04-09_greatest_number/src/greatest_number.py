def greatest_number(num0, num1, num2):
    if ((num0 >= num1) and (num1 >= num2)) or ((num0 >= num2) and (num2 >= num1)):
        return num0
    elif ((num1 >= num2) and (num2 >= num0)) or ((num1 >= num0) and (num0 >= num2)):
        return num1
    elif ((num2 >= num0) and (num0 >= num1)) or ((num2 >= num1) and (num1 >= num0)):
        return num2
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)