attempts = 0
while True:
    correct_pin = 4321
    input_pin = int(input("PIN: "))
    attempts += 1
    if (input_pin == correct_pin) and (attempts == 1):
        print("Correct! It only took you one single attempt!")
        break
    elif input_pin == correct_pin:
        print(f"Correct! It took you {attempts} attempts")
        break
    elif (input_pin != correct_pin):
        print("Wrong")